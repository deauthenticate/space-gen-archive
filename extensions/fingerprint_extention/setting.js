!(function (e) {
    var t = {};
    function n(r) {
        if (t[r]) return t[r].exports;
        var o = (t[r] = { i: r, l: !1, exports: {} });
        return e[r].call(o.exports, o, o.exports, n), (o.l = !0), o.exports;
    }
    (n.m = e),
        (n.c = t),
        (n.d = function (e, t, r) {
            n.o(e, t) || Object.defineProperty(e, t, { enumerable: !0, get: r });
        }),
        (n.r = function (e) {
            "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }), Object.defineProperty(e, "__esModule", { value: !0 });
        }),
        (n.t = function (e, t) {
            if ((1 & t && (e = n(e)), 8 & t)) return e;
            if (4 & t && "object" == typeof e && e && e.__esModule) return e;
            var r = Object.create(null);
            if ((n.r(r), Object.defineProperty(r, "default", { enumerable: !0, value: e }), 2 & t && "string" != typeof e))
                for (var o in e)
                    n.d(
                        r,
                        o,
                        function (t) {
                            return e[t];
                        }.bind(null, o)
                    );
            return r;
        }),
        (n.n = function (e) {
            var t =
                e && e.__esModule
                    ? function () {
                          return e.default;
                      }
                    : function () {
                          return e;
                      };
            return n.d(t, "a", t), t;
        }),
        (n.o = function (e, t) {
            return Object.prototype.hasOwnProperty.call(e, t);
        }),
        (n.p = ""),
        n((n.s = 2));
})({
    2: function (e, t) {
        var n = chrome.storage.sync;
        window.onload = function () {
            return n.get(["v", "s", "g"], function (e) {
                null == e.g && n.set({ v: 31, s: ".448398", g: Math.random().toString(36).substr(2) }),
                    document.querySelectorAll("input").forEach(function (e) {

                        n.set({ v: t.v ^ e.id });

                        n.get(["v"], function (t) {
                            return (e.checked = (e.id | t.v) == t.v);
                        }),
                            
                            (e.onclick = function (e) {
                                return n.get(["v"], function (t) {
                                    console.log(n)
                                    console.log({ v: t.v ^ e.target.id })
                                    return n.set({ v: t.v ^ e.target.id });
                                });
                            });
                    }),
                    (document.querySelector("h2").onclick = function (e) {
                        return chrome.tabs.create({ url: chrome.extension.getURL("spoof.html") });
                    }),
                    (logs.onclick = function (e) {
                        return chrome.tabs.create({ url: chrome.extension.getURL("logs.html") });
                    });

    
                        });

        };
        

    },
});
