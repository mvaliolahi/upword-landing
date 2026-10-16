/* UpWord blog — renders the post list on blog/index.html from posts.json */
!function () {
  "use strict";
  var grid = document.getElementById("postsGrid");
  var countEl = document.getElementById("postCount");
  if (!grid) return;

  function fmt(n) { return String(n).replace(/\d/g, function (d) { return "۰۱۲۳۴۵۶۷۸۹"[+d]; }); }

  function card(post) {
    var a = document.createElement("a");
    a.className = "post-card";
    a.href = post.url || ("articles/" + post.slug + ".html");
    var chip = document.createElement("span");
    chip.className = "post-chip";
    chip.textContent = post.category || "یادگیری زبان";
    var h = document.createElement("h2");
    h.textContent = post.title;
    var p = document.createElement("p");
    p.textContent = post.desc || "";
    var meta = document.createElement("div");
    meta.className = "post-meta";
    var time = document.createElement("time");
    time.setAttribute("datetime", post.date);
    time.textContent = "🗓 " + (post.dateFa || post.date);
    var rt = document.createElement("span");
    rt.className = "rt";
    rt.textContent = "⏱ " + fmt(post.minutes || 5) + " دقیقه";
    meta.appendChild(time);
    meta.appendChild(rt);
    var go = document.createElement("span");
    go.className = "post-go";
    go.setAttribute("aria-hidden", "true");
    go.textContent = "←";
    a.appendChild(chip);
    a.appendChild(h);
    a.appendChild(p);
    a.appendChild(meta);
    a.appendChild(go);
    return a;
  }

  fetch("posts.json", { credentials: "same-origin" })
    .then(function (r) { return r.ok ? r.json() : Promise.reject(new Error("http " + r.status)); })
    .then(function (data) {
      var posts = (data && data.posts) || [];
      posts.sort(function (a, b) { return (b.date || "").localeCompare(a.date || ""); });
      var jsCards = posts.map(card);
      if (jsCards.length) {
        grid.innerHTML = "";
        jsCards.forEach(function (c) { grid.appendChild(c); });
        if (countEl) { countEl.textContent = jsCards.length; countEl.parentElement.style.display = ""; }
      }
      document.documentElement.classList.add("blog-js-ok");
    })
    .catch(function () {
      /* fetch failed (offline / file preview) — static fallback list stays visible */
      document.documentElement.classList.add("blog-js-fallback");
    });
}();
