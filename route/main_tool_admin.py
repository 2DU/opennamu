from .tool.func import *

def main_tool_admin():
    with get_db_connect() as conn:
        return easy_minify(conn, flask.render_template(skin_check(conn),
            imp = [get_lang(conn, 'admin_tool'), wiki_set(conn), wiki_custom(conn), wiki_css([0, 0])],
            data = render_simple_set(conn, '''
                <h2>''' + get_lang(conn, 'admin') + '''</h2>
                <ul class="opennamu_ul">
                    <li><a href="/manager/2">''' + get_lang(conn, 'acl_change') + '''</a></li>
                    <li><a href="/manager/3">''' + get_lang(conn, 'check_user') + '''</a></li>
                    <li><a href="/auth/give/ban">''' + get_lang(conn, 'ban') + '''</a></li>
                    <li><a href="/auth/give/ban_multiple">''' + get_lang(conn, 'multiple_ban') + '''</a></li>
                    <li><a href="/manager/17">''' + get_lang(conn, 'release') + '''</a></li>
                    <li><a href="/manager/5">''' + get_lang(conn, 'authorize') + '''</a></li>
                </ul>
                <h2>''' + get_lang(conn, 'owner') + '''</h2>
                <ul class="opennamu_ul">
                    <li><a href="/auth/list">''' + get_lang(conn, 'admin_group_list') + '''</a></li>
                    <li><a href="/delete_multiple">''' + get_lang(conn, 'many_delete') + '''</a></li>
                    <li><a href="/app_submit">''' + get_lang(conn, 'application_list') + '''</a></li>
                    <li><a href="/register">''' + get_lang(conn, 'add_user') + '''</a></li>
                    <li><a href="/setting">''' + get_lang(conn, 'setting') + '''</a></li>
                    <li><a href="/manager/18">''' + get_lang(conn, 'user_fix') + '''</a></li>
                </ul>
                <h3>''' + get_lang(conn, 'filter') + '''</h3>
                <ul class="opennamu_ul">
                    <li><a href="/filter/edit_filter">''' + get_lang(conn, 'edit_filter_list') + '''</a></li>
                    <li><a href="/filter/inter_wiki">''' + get_lang(conn, 'interwiki_list') + '''</a></li>
                    <li><a href="/filter/edit_top">''' + get_lang(conn, 'edit_tool_list') + '''</a></li>
                    <li><a href="/filter/image_license">''' + get_lang(conn, 'image_license_list') + '''</a></li>
                    <li><a href="/filter/email_filter">''' + get_lang(conn, 'email_filter_list') + '''</a></li>
                    <li><a href="/filter/name_filter">''' + get_lang(conn, 'id_filter_list') + '''</a></li>
                    <li><a href="/filter/file_filter">''' + get_lang(conn, 'file_filter_list') + '''</a></li>
                    <li><a href="/filter/extension_filter">''' + get_lang(conn, 'extension_filter_list') + '''</a></li>
                    <li><a href="/filter/document">''' + get_lang(conn, 'document_filter_list') + '''</a></li>
                    <li><a href="/filter/outer_link">''' + get_lang(conn, 'outer_link_filter_list') + '''</a> (''' + get_lang(conn, 'beta') + ''')
                    <li><a href="/filter/template">''' + get_lang(conn, 'template_document_list') + '''</a> (''' + get_lang(conn, 'beta') + ''')
                </ul>
                <h3>''' + get_lang(conn, 'server') + '''</h2>
                <ul class="opennamu_ul">
                    <li><a href="/restart">''' + get_lang(conn, 'wiki_restart') + '''</a></li>
                    <li><a href="/shutdown">''' + get_lang(conn, 'wiki_shutdown') + '''</a></li>
                    <li><a href="/update">''' + get_lang(conn, 'update') + '''</a></li>
                </ul>
                <h2>''' + get_lang(conn, 'version') + '''</h2>
                <ul class="opennamu_ul">
                    <li id="ver_send_2">''' + get_lang(conn, 'version') + ''' : </li>
                    <li id="ver_send">''' + get_lang(conn, 'lastest') + ''' : </li>
                </ul>
                <h3>''' + get_lang(conn, 'skin_info') + '''</h3>
                <ul class="opennamu_ul">
                    <li><a href="/api/skin_info?all=true">''' + get_lang(conn, 'skin_info') + '''</a></li>
                    <div id="ver_send_3"></div>
                </ul>
                <!-- JS : opennamu_do_insert_version -->
                <!-- JS : opennamu_do_insert_version_skin -->
            '''),
            menu = [['other', get_lang(conn, 'return')]]
        ))