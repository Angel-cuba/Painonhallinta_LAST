DROP VIEW "main"."henkilo_miitaus_ika";
CREATE VIEW henkilo_miitaus_ika AS
SELECT henkilo.henkilo_id, henkilo.sukunimi, henkilo.etunimi, mittaus.mittaus_id, mittaus.pituus, mittaus.paino, henkilo.spaiva, date('now') AS tanaan, (julianday('now') - julianday(henkilo.spaiva))/365 AS ika
FROM henkilo LEFT OUTER JOIN mittaus ON henkilo.henkilo_id = mittaus.henkilo_id