from .tool.func import *

from .edit import edit_editor

def recent_history_add(name = 'Test', do_type = ''):
    with get_db_connect() as conn:
        curs = conn.cursor()

        ip = ip_check()
        if admin_check(conn) != 1:
            return re_error(conn, '/ban')

        if flask.request.method == 'POST':
            admin_check(conn, None, 'history_add (' + name + ')')

            today = get_time()
            content = flask.request.form.get('content', '')
            leng = '+' + str(len(content))

            history_plus(conn, 
                name,
                content,
                today,
                'Add:' + flask.request.form.get('get_ip', ''),
                flask.request.form.get('send', ''),
                leng,
                mode = 'add'
            )

            conn.commit()

            return redirect(conn, '/history/' + url_pas(name))
        else:            
            return easy_minify(conn, flask.render_template(skin_check(conn),
                imp = [get_lang(conn, 'history_add'), wiki_set(conn), wiki_custom(conn), wiki_css(['(' + name + ')', 0])],
                data = '''
                    <form method="post">
                        <input placeholder="''' + get_lang(conn, 'why') + '''" name="send">
                        <hr class="main_hr">
                        
                        <input placeholder="''' + get_lang(conn, 'name') + '''" name="get_ip">
                        <hr class="main_hr">

                        ''' + edit_editor(curs, ip) + '''
                    </form>
                ''',
                menu = [['history/' + url_pas(name), get_lang(conn, 'return')]]
            ))