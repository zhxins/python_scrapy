import re

a = '[<script>window.onload=function(){location.href="http://www.36605558.com/index.php?url=http://www.iqiyi.com/v_19rrb2yq04.html?fc=8b62d5327a54411b";}</script>]'
pattern = re.compile("url : '(.+)',", re.IGNORECASE)
pattern2 = re.compile('url=(.+)')
url = pattern2.findall(a)
print(url)

pattern1 = re.compile('23(.+)')
result = pattern1.findall('as3SiOPdj#@23awe')
print(result)