from .tool.func import *

def bbs_w_set(bbs_num = ''):
    with get_db_connect() as conn:
        curs = conn.cursor()

        curs.execute(db_change('select set_data from bbs_set where set_id = ? and set_name = "bbs_name"'), [bbs_num])
        db_data = curs.fetchall()
        if not db_data:
            return redirect(conn, '/bbs/main')
        else:
            bbs_name = db_data[0][0]
        
        bbs_num_str = str(bbs_num)

        i_list = ['bbs_acl', 'bbs_edit_acl', 'bbs_comment_acl', 'bbs_view_acl', 'bbs_markup']

        if flask.request.method == 'POST':
            if acl_check('', 'owner_auth', '', '', 'bbs_set (acl)') == 1:
                return re_error(conn, 0)
            else:
                for for_a in range(len(i_list)):
                    curs.execute(db_change("update bbs_set set set_data = ? where set_name = ? and set_id = ?"), [
                        flask.request.form.get(i_list[for_a], 'normal'),
                        i_list[for_a],
                        bbs_num
                    ])

                return redirect(conn, '/bbs/set/' + bbs_num_str)
        else:
            d_list = ['' for _ in range(0, len(i_list))]

            other_menu = []
            if acl_check('', 'bbs_auth', '', '') == 1:
                disable = 'disabled'
            else:
                disable = ''
                other_menu += [['bbs/delete/' + bbs_num_str, get_lang(conn, 'delete')]]

            for for_a in range(len(i_list)):
                curs.execute(db_change('select set_data from bbs_set where set_name = ? and set_id = ?'), [i_list[for_a], bbs_num])
                sql_d = curs.fetchall()
                if sql_d:
                    d_list[for_a] = sql_d[0][0]
                else:
                    curs.execute(db_change('insert into bbs_set (set_name, set_code, set_id, set_data) values (?, "", ?, ?)'), [i_list[for_a], bbs_num, 'normal'])
                    d_list[for_a] = 'normal'

            acl_div = ['' for _ in range(0, len(i_list))]
            acl_list = get_acl_list()
            for for_a in range(0, len(i_list)):
                if for_a == 4:
                    acl_list = ['normal'] + get_init_set_list('markup')['list']

                for data_list in acl_list:
                    if data_list == d_list[for_a]:
                        check = 'selected="selected"'
                    else:
                        check = ''

                    acl_div[for_a] += '<option value="' + data_list + '" ' + check + '>' + (data_list if data_list != '' else 'normal') + '</option>'

            return easy_minify(conn, flask.render_template(skin_check(conn),
                imp = [get_lang(conn, 'bbs_set'), wiki_set(conn), wiki_custom(conn), wiki_css(['(' + bbs_name + ')', 0])],
                data = render_simple_set(conn, '''
                    <form method="post">
                        <hr class="main_hr">
                        <a href="/acl/TEST#exp">(''' + get_lang(conn, 'reference') + ''')</a>
                        
                        <h2>''' + get_lang(conn, 'acl') + '''</h2>
                        <h3>''' + get_lang(conn, 'bbs_view_acl') + '''</h3>
                        <select ''' + disable + ''' name="bbs_view_acl">''' + acl_div[3] + '''</select>

                        <h4>''' + get_lang(conn, 'bbs_acl') + '''</h4>
                        <select ''' + disable + ''' name="bbs_acl">''' + acl_div[0] + '''</select>

                        <h5>''' + get_lang(conn, 'bbs_edit_acl') + '''</h5>
                        <select ''' + disable + ''' name="bbs_edit_acl">''' + acl_div[1] + '''</select>

                        <h5>''' + get_lang(conn, 'bbs_comment_acl') + '''</h5>
                        <select ''' + disable + ''' name="bbs_comment_acl">''' + acl_div[2] + '''</select>

                        <h2>''' + get_lang(conn, 'markup') + '''</h2>
                        <select ''' + disable + ''' name="bbs_markup">''' + acl_div[4] + '''</select>
                        
                        <hr class="main_hr">
                        <button id="opennamu_save_button" type="submit">''' + get_lang(conn, 'save') + '''</button>
                    </form>
                '''),
                menu = [['bbs/in/' + bbs_num_str, get_lang(conn, 'return')]] + other_menu
            ))