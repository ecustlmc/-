import datetime
def ListBeauty(L):
    n = len(L)
    html = """
    <table border="1">
    """
    block = ""
    for each in L:
        block = """
        <tr>
        """
        for eac in each:
            block += """<td>%s</td>"""%str(eac)
        block += """
        </tr>"""
        html += block
    html = html + """
    </table>
    """
    return html
    #return html.format(block = block.format(td = td))


if __name__ == "__main__":
    L = [('10162600', '李明辰', '2018571', '泛函分析random', datetime.datetime(2018, 12, 6, 9, 23), 'Random101')]
    a = ListBeauty(L)
    print(a)
