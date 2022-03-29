"use strict";

function opennamu_do_id_check(data) {
    if(data.match(/\.|\:/)) {
        return 0;
    } else {
        return 1;
    }
}

function opennamu_do_url_encode(data) {
    return encodeURIComponent(data);
}

function opennamu_do_user_document_check() {
    let data_all = document.getElementsByClassName('opennamu_user_link');
    for(let for_a = 0; for_a < data_all.length; for_a++) {
        if(data_all && data_all[for_a]) {
            if(data_all[for_a].getAttribute('complete') === '1') {
                continue;
            }
        }
        
        let data = data_all[for_a].innerHTML;
        
        let xhr = new XMLHttpRequest();
        xhr.open("POST", "/api/user_info/" + opennamu_do_url_encode(data));
        xhr.send();
        
        document.getElementsByClassName('opennamu_user_link')[for_a].setAttribute('complete', '1');
        xhr.onreadystatechange = function() {
            if(this.readyState === 4 && this.status === 200) {
                let xhr_data = JSON.parse(this.responseText);
                if(xhr_data[data]['document'] === 0) {
                    document.getElementsByClassName('opennamu_user_link')[for_a].id = "not_thing";
                }
                
                if(xhr_data[data]['auth'] === 0) {
                    
                } else if(xhr_data[data]['auth'] === 1) {
                    
                } else {
                    document.getElementsByClassName('opennamu_user_link')[for_a].innerHTML += "✅";
                }
            }
        }
    }
}

function opennamu_do_ip_parser() {
    let data_all = document.getElementsByClassName('opennamu_ip_render');
    let data_list = {};
    for(let for_a = 0; for_a < data_all.length; for_a++) {
        if(data_all && data_all[for_a]) {
            if(data_all[for_a].getAttribute('complete') === '1') {
                continue;
            }
        }
        
        let data = data_all[for_a].innerHTML;
        let data_raw = data;
        
        if(data_list[data_raw]) {
            document.getElementsByClassName('opennamu_ip_render')[for_a].innerHTML = data_list[data_raw];
            document.getElementsByClassName('opennamu_ip_render')[for_a].setAttribute('complete', '1');
            
            continue;
        }
        
        if(opennamu_do_id_check(data_raw)) {
            data = '' + 
                '<a class="opennamu_user_link" ' + 
                    'href="/w/user:' + opennamu_do_url_encode(data_raw) + '">' + 
                    data_raw + 
                '</a>' +
            '';
        } else {
            
        }
        
        data += ' <a href="/user/' + opennamu_do_url_encode(data_raw) + '">(🛠︎)</a>';

        document.getElementsByClassName('opennamu_ip_render')[for_a].innerHTML = data;
        document.getElementsByClassName('opennamu_ip_render')[for_a].setAttribute('complete', '1');

        data_list[data_raw] = data;
    }
    
    opennamu_do_user_document_check();
}

document.addEventListener("DOMContentLoaded", opennamu_do_ip_parser);