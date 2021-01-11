/** layuiAdmin.std-v1.2.1 LPPL License By http://www.layui.com/admin/ */
;layui.define(["admin", "table", "util"], function (e) {
    var t = layui.$, i = (layui.admin, layui.table), l = (layui.element, {
        all: {text: "全部消息", id: "LAY-app-message-all"},
    }), a = function (e) {
        return e.title
    };
    i.render({
        elem: "#LAY-app-message-all",
        url: '/messages',
        page: !0,
        cols: [[{type: "checkbox", fixed: "left"}, {
            field: "title",
            title: "标题内容",
            minWidth: 300,
            templet: a
        }, {field: "time", title: "时间", width: 170, templet: "<div>{{ layui.util.timeAgo(d.time) }}</div>"}]],
        skin: "line"
    });
    var d = {
        del: function (e, t) {
            var a = l[t], d = i.checkStatus(a.id), s = d.data;
            return 0 === s.length ? layer.msg("未选中行") : void layer.confirm("确定删除选中的数据吗？", function () {
                layer.msg("删除成功", {icon: 1}), i.reload(a.id)
            })
        }, ready: function (e, t) {
            var a = l[t], d = i.checkStatus(a.id), s = d.data;
            return 0 === s.length ? layer.msg("未选中行") : (
                $.ajax({
                    url: "/mark_read/",
                    type: "post",
                    data: {
                        "msg": s,
                    },
                    success: function (data) {
                        if (data) {
                            layer.msg("标记已读成功", {icon: 1}), void i.reload(a.id);
                        } else {
                            console.log('?');
                        }
                    }
                }))
        }, readyAll: function (e, t) {
            var i = l[t];
            $.ajax({
                url: "/mark_read/",
                type: "get",
                success: function (data) {
                    if (data) {
                        layer.msg(i.text + "：全部已读", {icon: 1});
                        $('.layui-badge').text(0);
                    }
                }
            })
        }
    };
    t(".LAY-app-message-btns .layui-btn").on("click", function () {
        var e = t(this), i = e.data("events"), l = e.data("type");
        d[i] && d[i].call(this, e, l)
    }), e("message", {})
});