function! ConvertElispGaijiToPython()
    %s/;/#/g     "comments
    %s/("\([hz]\)\(.*\)" "\(.*\)")/0x\2: u'\3',/g
   "s/\<./\u&/g   "Built-in substitution capitalizes each word
   "center        "Built-in center command centers entire line
   "+1            "Built-in relative motion (+1 line down)
endfunction

