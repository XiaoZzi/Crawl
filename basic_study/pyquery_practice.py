from pyquery import PyQuery

doc = '''
<div class="blEntry address  clickable colCnt3"onclick="ta.prwidgets.call('handlers.onAddressClicked', event, this);"data-mapFilters="">
<span class="ui_icon map-pin"></span>
<span class="street-address">Clive Steps</span> | 
<span class="extended-address">King Charles Street</span>, 
<span class="locality">London SW1A 2AQ, </span>
England
</div>
'''

content = PyQuery(doc)
print(content('.blEntry.address .street-address').text() + ' ' +
      content('.blEntry.address .extended-address').text() + ' ' +
      content('.blEntry.address .locality').text())
print(content('.blEntry.address').text())
