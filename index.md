---
layout: default
title: Latexcursus
---

<div class="page-header">
<h1>Latexcursus <small>Bachelor Wiskunde UvA</small></h1>
</div>

## Lessen 
{% for week in site.data.weeks %}
<h4>Week {{ week.number }} </h4>
{% assign t = 1 %}
<dl>
  {% for lesson in site.data.lessons %}
  {% if lesson.week == week.number %}
    <dt><a href="/lessons/{{ lesson.url }}">{{ t }}. {{ lesson.title }}</a></dt>
    <dd>{{ lesson.desc }}</dd>
  {% assign t = t | plus: 1 %}
  {% endif %}
  {% endfor %}
</dl>
{% endfor %}

---
## Voorwoord
De inhoud van deze lessen is voor een groot deel afkomstig van [Latex Wikibooks](http://en.wikibooks.org/wiki/LaTeX).


