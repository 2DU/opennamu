from .tool.func import *

def recent_history_reset(name = 'Test'):
    with get_db_connect() as conn:
        curs = conn.cursor()

        if admin_check(conn) != 1:
            return re_error(conn, '/error/3')

        if flask.request.method == 'POST':
            admin_check(conn, None, 'history reset ' + name)

            curs.execute(db_change("delete from history where title = ?"), [name])
            conn.commit()

            return redirect(conn, '/history/' + url_pas(name))
        else:
            return easy_minify(conn, flask.render_template(skin_check(conn),
                imp = [name, wiki_set(conn), wiki_custom(conn), wiki_css(['(' + get_lang(conn, 'history_reset') + ')', 0])],
                data = '''
                    <form method="post">
                        <span>''' + get_lang(conn, 'delete_warning') + '''</span>
                        <hr class="main_hr">
                        <button type="submit">''' + get_lang(conn, 'reset') + '''</button>
                    </form>
                ''',
                menu = [['history/' + url_pas(name), get_lang(conn, 'return')]]
            ))