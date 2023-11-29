# String to Skill List

Dieser Endpoint nimmt den aus der Anforderungsfile stammenden Text entgegen.

## DB Anforderungs Liste

Aus dem Text werden zum einen Anforderungs KeyWords genommen, die häufig in DB Ausschreubungen genannt werden. Es wird in der Antwort im JSON Eine Liste dieser Anforderungsbegriffe zurückgegeben

## Decidalo Match Liste

die Liste an Anforderungen wird erweitert zu einer Liste an breitgefassten decidalo Skills, um einen direkten Vergleich zu ermöglichen. Wird zusätzlich als JSON zurückgegeben.

POST data={"text" : <yourText>} to https://stringtoskilllist.shigeocst.repl.co/StringToSkillList
returns {"ListeAnforderungen" : <ListeAnforderungen>, "decidaloMatchList" : <textSplit>}