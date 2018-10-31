from collections import namedtuple
import datetime as dt
from shutil import copyfile
import os

from fpdf import FPDF, HTMLMixin

Insight = namedtuple('Insight', 'title text img source')


def make_report(insights, move=False, month_end=False, date=dt.date.today()):
    pdf = ReportPDF()
    print('Adding cover page...')
    pdf.add_page()
    pdf.image('logo.png', x=85, y=155, w=40)
    pdf.ln(100)
    pdf.set_font('Helvetica', 'B', 36)
    pdf.cell(0, 0, 'Snake Population Report', 0, 0, 'C')
    pdf.ln(20)
    pdf.set_font('Helvetica', 'B', 20)
    if month_end:
        previous_month = date.replace(month=date.month - 1).strftime('%B %Y')
        pdf.cell(0, 0, 'for the month of {}'.format(previous_month), 0, 0, 'C')
    else:
        report_date = date.strftime('%d %B %Y')
        pdf.cell(0, 0, 'for the week ending {}'.format(report_date), 0, 0, 'C')

    numdate = date.strftime('%Y%m%d')  # looks like 20180914
    new_dir = r'{}'.format(numdate)
    if not os.path.exists(new_dir):
        print('Creating new directory for report...')
        os.makedirs(new_dir)

    for index, insight in enumerate(insights):
        print('Creating page {}'.format(index + 1))
        pdf.add_page()
        if insight.img:
            pdf.image(insight.img, x=15, y=130, w=180)
        pdf.ln(10)
        pdf.set_font('Helvetica', 'B', 20)
        pdf.multi_cell(
            200,
            12,
            txt='Insight {}. {}'.format(str(index + 1), insight.title),
            align='L')
        pdf.ln(10)
        pdf.set_font('Helvetica', size=10)
        pdf.multi_cell(190, 10, txt=insight.text, align='L')
        pdf.ln(10)
        pdf.set_font('Helvetica', size=8)
        pdf.write_html('<a HREF="{}">Source</a>'.format(insight.source))
        if move:
            print('Moving {} to the new directory...'.format(insight.img))
            os.rename(insight.img, '{}/{}'.format(numdate, insight.img))

    print('Saving report...')
    pdf.output('{}/{}.pdf'.format(numdate, numdate))
    print('Copying report script to directory...')
    copyfile('report.py'.format(numdate), '{}/report.py'.format(numdate))
    print('All done! Have a super day.')


class ReportPDF(FPDF, HTMLMixin):
    # 210 × 297 millimeters

    def footer(self):
        self.set_y(-10)
        self.set_font('Arial', 'I', 8)

        # Add a page number
        page = 'Page ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')
