import codecs
file_path = 'templates/biodata/mangalfera_summelen_from.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

start_marker = '<!-- INFO BANNER -->'
end_marker = '<!-- FORM -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_banner = '''<!-- INFO BANNER -->
  <div class="info-banner" style="text-align: left; line-height: 1.6; font-size: 0.98em;">
    <strong style="font-size: 1.1em; color: #991B1B;">*સર્વજ્ઞાતિ Biodata Booklet* :</strong><br>
    સનાતન ગુજરાતી હિન્દૂ સમાજ ની બાયોડેટા બુકલેટ બની રહી છે. (બ્રાહ્મણ, પટેલ, વૈષ્ણવ, જૈન, સોની વગેરે... જેમણે જ્ઞાતિબાધ નથી તેમના માટે)<br><br>

    <span class="chk">&#10004;</span> MangalFera.in Website members - યુવક યુવતીઓ બંને માટે Free Registration &amp; Free E-Booklet મળશે.<br>
    <span class="chk">&#10004;</span> અન્ય બધાજ યુવક - યુવતીઓ માટે Registration Fees = Rs 500 (સાથે 1 Booklet મળશે). અથવા Rs 300 (સાથે 1 PDF મળશે).<br><br>

    <div style="background: #FEF2F2; padding: 12px; border-radius: 8px; border: 1px dashed #FCA5A5; font-size: 0.95em; color: #991B1B;">
      (ઉમેદવાર ના નામ તથા અન્ય વિગતો સાથે, આ Form ભરીને સબમિટ કરશો, પછી તમને 24 કલાક મા અમારી અમદાવાદ - વડોદરા ઓફિસ થી વેરિફિકેશન ફૉન કૉલ આવશે)
    </div>
  </div>
  
  '''
    content = content[:start_idx] + new_banner + content[end_idx:]
    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(content)
    print('Banner successfully updated.')
else:
    print('Could not find markers.')
