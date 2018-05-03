# coding:utf-8
class HtmlOutputer(object):
    def __init__(self):
        self.datas =[]

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write("<html>")
        fout.write("<body><center>")


        #默认ascii
        for data in self.datas:
            fout.write("<table border='1'width='1000px' bgcolor='Thistle'>")
            fout.write("<tr>")
            fout.write("<td width='100px'>url</td><td><h5>%s</h5></td></tr><tr>" % data['url'].encode('utf-8'))
            fout.write("<td width='100px'>标题</td><td><h3>%s</h3></td></tr><tr>" % data['title'])
            fout.write("<td width='100px'>简介</td><td>%s</td></tr><tr>" % data['summary'])
            fout.write("</tr>")
            fout.write("</table>")
            fout.write("<br><br>")
        fout.write("</center></body>")
        fout.write("</html>")
        fout.close()