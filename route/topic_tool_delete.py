from .tool.func import *

def topic_tool_delete(topic_num = 1):
    with get_db_connect() as conn:
        curs = conn.cursor()

        if admin_check(conn, None) != 1:
            return re_error(conn, '/error/3')

        topic_num = str(topic_num)

        if flask.request.method == 'POST':
            curs.execute(db_change("delete from topic where code = ?"), [topic_num])
            curs.execute(db_change("delete from rd where code = ?"), [topic_num])
            conn.commit()

            return redirect(conn, '/')
        else:
            return easy_minify(conn, flask.render_template(skin_check(conn),
                imp = [get_lang(conn, 'topic_delete'), wiki_set(conn), wiki_custom(conn), wiki_css([0, 0])],
                data = '''
                    <form method="post">
                        <span>''' + get_lang(conn, 'delete_warning') + '''</span>
                        <hr class="main_hr">
                        <button type="submit">''' + get_lang(conn, 'delete') + '''</button>
                    </form>
                ''',
                menu = [['thread/' + topic_num + '/tool', get_lang(conn, 'return')]]
            ))