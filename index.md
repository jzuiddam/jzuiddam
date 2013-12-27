---
layout: default
title: Latexcursus
---

<div class="page-header">
<h1>Latexcursus <small>Bachelor Wiskunde UvA</small></h1>
</div>

## Lessen 
{% for week in site.weeks %}
<h4>Week {{ week.number }} </h4>
<dl>
  {% for lesson in site.lessons %}
  {% if lesson.week == week.number %}
    <dt><a href="{{ lesson.url }}">{{ lesson.title }}</a></dt>
    <dd>{{ lesson.desc }}</dd>
  {% endif %}
  {% endfor %}
</dl>
{% endfor %}

---
## Voorwoord
De inhoud van deze lessen is voor een groot deel afkomstig van [Latex Wikibooks](http://en.wikibooks.org/wiki/LaTeX).


