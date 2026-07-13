from app.processors.text_chunker import TextChunker

sample_text = """
Artificial Intelligence is transforming industries across the world.

Machine Learning enables systems to learn from data.

Deep Learning is a subset of Machine Learning.

Large Language Models power intelligent assistants.

Enterprise Intelligence OS combines AI, RAG, and multi-agent workflows
to build enterprise-grade knowledge systems.
""" * 20

chunker = TextChunker()

chunks = chunker.chunk(sample_text)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print("=" * 60)
    print(f"Chunk {i+1}")
    print(chunk[:200])