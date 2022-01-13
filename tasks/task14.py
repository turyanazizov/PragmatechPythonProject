# 14. word = “istədiyiniz sözü yaza bilərsiz” məsələn word = ‘culture’ “Nineteet Eighty-Four does not present "art-as-culture" but "art-as-function"cüməsini bir dəyişkənə mənimsədin və həmin dəyişkəndə saxlayın və word-ə verdiyiniz sözün bu dəyişkəndə olub-olmamasını yoxlayın. Əgər söz varsa, ekranda belə bir nəticə çıxarın; “Culture” sözü mətndə var. Əgər yoxdursa, “Not found” çapa verin. 
word='culture'
sentence='Nineteet Eighty-Four does not present "art-as-culture" but "art-as-function"'
if sentence.find(word)>0:
    print('Word Found')
else:
    print("Word NOT Found")