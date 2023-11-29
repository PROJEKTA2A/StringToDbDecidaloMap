# String to DB-Decidalo-Map

Dieser Endpoint nimmt den aus der Anforderungsfile stammenden Text entgegen und liefert eine Map mit DB Anforderungen als Keys und dazu jeweils passende Listen mit Decidalo Skills

## Senden der POST Request

POST data={"text" : yourText} to https://stringtodbdecidalomap.shigeocst.repl.co/StringToDbDecidaloMap ->
returns {"DbDecidaloMap" : DbDecidaloMap}
