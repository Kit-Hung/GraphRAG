import os

from langchain_community.graphs import Neo4jGraph


def conf_neo4j():
    """
    设置连接图数据库的环境变量
    """
    os.environ["NEO4J_URI"] = "bolt://localhost:7687"
    os.environ["NEO4J_USERNAME"] = "neo4j"
    os.environ["NEO4J_PASSWORD"] = "neo4j"


def get_neo4j_graph():
    """
    获取 neo4j 客户端
    :return: neo4j 客户端
    """

    # 设置 neo4j 环境变量
    conf_neo4j()

    # 定义 neo4j 客户端
    graph = Neo4jGraph()
    print("Neo4j config successfully.")
    return graph


if __name__ == '__main__':
    get_neo4j_graph()
