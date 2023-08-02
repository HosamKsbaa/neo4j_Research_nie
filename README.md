


## Requirements
- Docker installed on your system.
- Internet access to fetch the sample graph data.

## Setup
To set up the Neo4j environment with the necessary plugins and import the sample data, follow the steps below:

1. Open a terminal or command prompt.

2. Execute the following Docker command to run the Neo4j instance with the required plugins:
   ```
   docker run --name testneo4j -p 7474:7474 -p 7687:7687 -d --env NEO4JLABS_PLUGINS='["apoc", "n10s"]' --env NEO4J_AUTH=none neo4j:5.7
   ```

## Data Import
The next step is to import the sample graph data into the Neo4j database. We'll use the `n10s` plugin to fetch the data from the specified URL and load it into the database.

1. Open a web browser and navigate to the Neo4j browser at http://localhost:7474.

2. In the Neo4j browser, execute the following Cypher queries one by one:

   a. Initialize the `n10s` plugin configuration and create a constraint to ensure unique URIs for resources:
      ```cypher
      CALL n10s.graphconfig.init();
      CREATE CONSTRAINT n10s_unique_uri FOR (r:Resource) REQUIRE r.uri IS UNIQUE;
      ```

   b. Import the sample data from the specified URL (https://raw.githubusercontent.com/wala/graph4code/master/sample_graph/stackoverflow_triples_sample.nq) in N-Quads format:
      ```cypher
      CALL n10s.rdf.import.fetch("https://raw.githubusercontent.com/wala/graph4code/master/sample_graph/stackoverflow_triples_sample.nq", "N-Quads", { singleTx: false });
      ```

## Data Deletion
Before running any analysis queries, you might want to delete any existing data to start with a clean slate. To delete all nodes and relationships in the database, execute the following query in the Neo4j browser:

```cypher
MATCH (n)
OPTIONAL MATCH (n)-[r]-()
DELETE n, r;
```

## Explore Data
Now that the data is imported, you can explore it using Cypher queries. For example, to get all nodes and relationships in the database, execute the following query:

```cypher
MATCH (s)-[p]->(o)
RETURN s, p, o;
```

Feel free to modify and execute other Cypher queries to analyze the data based on your research requirements.

## Note
Remember to stop and remove the Docker container when you are done with your research:

```
docker stop testneo4j
docker rm testneo4j
```

## References
- Neo4j: https://neo4j.com/
- Graph4Code: https://github.com/wala/graph4code

## License
This research work is provided under the [MIT License](LICENSE).
