from langchain_community.document_loaders import WikipediaLoader
from langchain.text_splitter import TokenTextSplitter


def get_split_doc(query):
    """
    加载维基百科上的文档，并将文档分割成小块
    :param query: 作为关键字搜素维基百科上的文档
    :return: 切分后的文档列表
    """

    # 创建维基百科 loader 对象，用于从维基百科加载文档
    # 通过 query 参数传递用户查询的关键字
    # load_max_docs=1 表示指定最多只加载一篇文档
    # 调用 load() 方法实际加载文档，赋值给 raw_documents 对象
    raw_documents = WikipediaLoader(query=query, load_max_docs=1).load()

    # 定义一个 token 切分器
    # chunk_size: 指定每个文本块的目标大小, 单位：字符
    # chunk_overlap: 指定相邻文本块之间重叠的字符数
    text_splitter = TokenTextSplitter(chunk_size=512, chunk_overlap=24)

    # 使用 token 切分器实际切加载的文档
    # raw_documents[:3] 只切 raw_documents 返回的 3 篇文档
    documents = text_splitter.split_documents(raw_documents[:3])
    print("Load and Split document successfully.")
    return documents


if __name__ == '__main__':
    print(len(get_split_doc("Elizabeth I")))
