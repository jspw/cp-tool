# Declare Varibale tags

table_start = "<table>"
table_end = "</table>"
table_row_start = "<tr>"
table_row_end = "</tr>"
table_head_start = "<th>"
table_head_end = "</th>"
table_data_start = "<td>"
table_data_end = "</td>"
href = "href="
link_start = "<a "
end = ">"
link_end = "</a>"
new_line = "\n"

def tableDataCreate(data):
    # "<td>data</td>"
    html = table_data_start + data + table_data_end
    # print(html)
    return html


def linkCreate(link, value):
    # "<a href="link" > value </a>"
    html = link_start + href + link + end + value + link_end
    return html

# def tableRow(n,datas):
#     for i in range(datas):

