# neo4j_Research_nie



docker run     --name testneo4j     -p7474:7474 -p7687:7687     -d      --env NEO4JLABS_PLUGINS='["apoc", "n10s"]'     --env NEO4J_AUTH=none     neo4j:5.7

call n10s.graphconfig.init()
CREATE CONSTRAINT n10s_unique_uri FOR (r:Resource) REQUIRE r.uri IS UNIQUE
call n10s.rdf.import.fetch("https://raw.githubusercontent.com/wala/graph4code/master/sample_graph/stackoverflow_triples_sample.nq" ,"N-Quads",{ singleTx: false } )





deleted 
MATCH (n)
OPTIONAL MATCH (n)-[r]-()
DELETE n, r;

get all 
MATCH (s)-[p]->(o)
RETURN s, p, o;
