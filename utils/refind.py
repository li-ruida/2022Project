import re
import requests

li='freeCodeCamp/freeCodeCamp'


now_link1='https://github.com/'+li
res=requests.get(now_link1)
res.encoding="utf-8"
# dom = bs4.BeautifulSoup(res.text, features="html.parser")
# print(dom.prettify())
stars=re.findall(fr'''<span id="repo-stars-counter-star" aria-label="(.*?) users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-turbo-replace="true" title="(.*?)" data-view-component="true" class="Counter js-social-count">(.*?)</span>''', res.text)
fork = re.findall(fr'''<span id="repo-network-counter" data-pjax-replace="true" data-turbo-replace="true" title="(.*?)" data-view-component="true" class="Counter">(.*?)</span>''',res.text)
watch=re.findall(fr'''</path>
</svg>
    <strong>(.*?)</strong>
    watching
</a></div>''',res.text)
contributors=re.findall(fr'''data-view-component="true" class="Link--primary no-underline">
    Contributors <span title="(.*?)" data-view-component="true" class="Counter">(.*?)</span>
</a>''',res.text)
commits=re.findall(fr'''                    <strong>(.*?)</strong>''',res.text)
license=re.findall(fr'''    <path fill-rule="evenodd" d="M8.75.75a.75.75 0 00-1.5 0V2h-.984c-.305 0-.604.08-.869.23l-1.288.737A.25.25 0 013.984 3H1.75a.75.75 0 000 1.5h.428L.066 9.192a.75.75 0 00.154.838l.53-.53-.53.53v.001l.002.002.002.002.006.006.016.015.045.04a3.514 3.514 0 00.686.45A4.492 4.492 0 003 11c.88 0 1.556-.22 2.023-.454a3.515 3.515 0 00.686-.45l.045-.04.016-.015.006-.006.002-.002.001-.002L5.25 9.5l.53.53a.75.75 0 00.154-.838L3.822 4.5h.162c.305 0 .604-.08.869-.23l1.289-.737a.25.25 0 01.124-.033h.984V13h-2.5a.75.75 0 000 1.5h6.5a.75.75 0 000-1.5h-2.5V3.5h.984a.25.25 0 01.124.033l1.29.736c.264.152.563.231.868.231h.162l-2.112 4.692a.75.75 0 00.154.838l.53-.53-.53.53v.001l.002.002.002.002.006.006.016.015.045.04a3.517 3.517 0 00.686.45A4.492 4.492 0 0013 11c.88 0 1.556-.22 2.023-.454a3.512 3.512 0 00.686-.45l.045-.04.01-.01.006-.005.006-.006.002-.002.001-.002-.529-.531.53.53a.75.75 0 00.154-.838L13.823 4.5h.427a.75.75 0 000-1.5h-2.234a.25.25 0 01-.124-.033l-1.29-.736A1.75 1.75 0 009.735 2H8.75V.75zM1.695 9.227c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L3 6.327l-1.305 2.9zm10 0c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L13 6.327l-1.305 2.9z"></path>
</svg>
     (.*?)
    </a>''',res.text)
language=re.findall(fr'''</path>
</svg>
          <span class="color-fg-default text-bold mr-1">(.*?)</span>
          <span>(.*?)</span>
        </a>
    </li>''',res.text)
description=re.findall(fr'''<div class="BorderGrid-cell">
            <h2 class="mb-3 h4">About</h2>

    <p class="f4 my-3">
      (.*?)
    </p>''',res.text)
date=re.findall(fr'''<relative-time datetime="(.*?)" class="no-wrap">(.*?)</relative-time>''',res.text)

now_link2='https://github.com/'+li+'/issues'
res=requests.get(now_link2)
res.encoding="utf-8"
# dom = bs4.BeautifulSoup(res.text, features="html.parser")
# print(dom.prettify())
issues_open=re.findall(fr'''      (.*?) Open(.*?)''', res.text)
issues_closed=re.findall(fr'''      (.*?) Closed(.*?)''', res.text)
now_project='freeCodeCamp/freeCodeCamp'
author=''
for tmpchar in now_project:
      if tmpchar=='/':
            break
      author+=tmpchar


now_link3='https://github.com/'+author
res=requests.get(now_link3)
res.encoding="utf-8"
followers=re.findall(fr'''<span class="text-bold color-fg-default">(.*?)</span>''', res.text)

