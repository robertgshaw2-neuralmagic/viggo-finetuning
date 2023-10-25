FROM mosaicml/llm-foundry:1.13.1_cu117-latest

RUN pip install jupyter

CMD ["/bin/bash"]

