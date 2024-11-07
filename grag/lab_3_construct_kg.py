from openai import base_url

from lab_1_load_split_doc import get_split_doc
from lab_2_conf_manage_neo4j import get_neo4j_graph
from langchain_openai import ChatOpenAI
from langchain_experimental.graph_transformers import LLMGraphTransformer


def construct_kg(query):
    # Define Neo4j client
    graph = get_neo4j_graph()

    # Define LLM and LLM Graph transformer
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm_transformer = LLMGraphTransformer(llm=llm)

    # Extract graph data
    # 把切片小文档转换为图文档
    graph_documents = llm_transformer.convert_to_graph_documents(get_split_doc(query))

    # Store to neo4j
    # 把图文档存储到 neo4j 数据库中
    # baseEntityLabel: True 意味着每个图文档实体都会被添加为图中的一个节点
    # include_source: True 意味着原始文档的元数据或上下文信息也可能被存储在图中
    graph.add_graph_documents(
        graph_documents,
        baseEntityLabel=True,
        include_source=True,
    )

    print("Construct Knowledge Graph successful.")


if __name__ == '__main__':
    construct_kg("Elizabeth I")
