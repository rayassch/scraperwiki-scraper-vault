<?php
# Blank PHP
$sourcescraper = 'select_committee_evidence';

$s = scraperwiki::getData($sourcescraper, $limit=250);
header('Content-type: application/json');
print "{ \"items\": ".json_encode($s) ."}";


?>
<?php
# Blank PHP
$sourcescraper = 'select_committee_evidence';

$s = scraperwiki::getData($sourcescraper, $limit=250);
header('Content-type: application/json');
print "{ \"items\": ".json_encode($s) ."}";


?>
