package route

import (
    "database/sql"

    jsoniter "github.com/json-iterator/go"
)

func Api_bbs_w_post_tabom(db *sql.DB, call_arg []string) string {
	var json = jsoniter.ConfigCompatibleWithStandardLibrary

    other_set := map[string]string{}
    json.Unmarshal([]byte(call_arg[0]), &other_set)

    return ""
}