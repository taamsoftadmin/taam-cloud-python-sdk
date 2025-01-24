# TaamCloud

Types:

```python
from taam_cloud.types import UploadResponse
```

Methods:

- <code title="post /upload">client.<a href="./src/taam_cloud/_client.py">upload</a>(\*\*<a href="src/taam_cloud/types/client_upload_params.py">params</a>) -> <a href="./src/taam_cloud/types/upload_response.py">UploadResponse</a></code>

# Embeddings

Types:

```python
from taam_cloud.types import EmbeddingsResponse
```

Methods:

- <code title="post /v1/embeddings">client.embeddings.<a href="./src/taam_cloud/resources/embeddings.py">create</a>(\*\*<a href="src/taam_cloud/types/embedding_create_params.py">params</a>) -> <a href="./src/taam_cloud/types/embeddings_response.py">object</a></code>

# Rerank

Methods:

- <code title="post /v1/rerank">client.rerank.<a href="./src/taam_cloud/resources/rerank.py">create</a>(\*\*<a href="src/taam_cloud/types/rerank_create_params.py">params</a>) -> None</code>

# Chat

## Completions

Methods:

- <code title="post /v1/chat/completions">client.chat.completions.<a href="./src/taam_cloud/resources/chat/completions.py">create</a>(\*\*<a href="src/taam_cloud/types/chat/completion_create_params.py">params</a>) -> None</code>

# Suno

## Music

Methods:

- <code title="post /suno/submit/music">client.suno.music.<a href="./src/taam_cloud/resources/suno/music.py">submit</a>(\*\*<a href="src/taam_cloud/types/suno/music_submit_params.py">params</a>) -> None</code>

# Models

Types:

```python
from taam_cloud.types import ModelListResponse
```

Methods:

- <code title="get /v1/models">client.models.<a href="./src/taam_cloud/resources/models.py">list</a>() -> <a href="./src/taam_cloud/types/model_list_response.py">ModelListResponse</a></code>

# Images

## Generations

Types:

```python
from taam_cloud.types.images import ImageGenerationResponse
```

Methods:

- <code title="post /v1/images/generations">client.images.generations.<a href="./src/taam_cloud/resources/images/generations.py">create</a>(\*\*<a href="src/taam_cloud/types/images/generation_create_params.py">params</a>) -> <a href="./src/taam_cloud/types/images/image_generation_response.py">ImageGenerationResponse</a></code>

# Crawl

Types:

```python
from taam_cloud.types import CrawlResponse, CrawlStatusResponse
```

Methods:

- <code title="post /v1/crawl">client.crawl.<a href="./src/taam_cloud/resources/crawl.py">create</a>(\*\*<a href="src/taam_cloud/types/crawl_create_params.py">params</a>) -> <a href="./src/taam_cloud/types/crawl_response.py">CrawlResponse</a></code>
- <code title="get /v1/crawl/{id}">client.crawl.<a href="./src/taam_cloud/resources/crawl.py">retrieve</a>(id) -> <a href="./src/taam_cloud/types/crawl_status_response.py">CrawlStatusResponse</a></code>

# Scrape

Types:

```python
from taam_cloud.types import ScrapeResponse
```

Methods:

- <code title="post /v1/scrape">client.scrape.<a href="./src/taam_cloud/resources/scrape.py">create</a>(\*\*<a href="src/taam_cloud/types/scrape_create_params.py">params</a>) -> <a href="./src/taam_cloud/types/scrape_response.py">ScrapeResponse</a></code>

# Maps

Types:

```python
from taam_cloud.types import MapResponse
```

Methods:

- <code title="post /v1/map">client.maps.<a href="./src/taam_cloud/resources/maps.py">discover</a>(\*\*<a href="src/taam_cloud/types/map_discover_params.py">params</a>) -> <a href="./src/taam_cloud/types/map_response.py">MapResponse</a></code>

# Searches

Types:

```python
from taam_cloud.types import SearchResponse
```

Methods:

- <code title="post /api/search">client.searches.<a href="./src/taam_cloud/resources/searches.py">perform</a>(\*\*<a href="src/taam_cloud/types/search_perform_params.py">params</a>) -> <a href="./src/taam_cloud/types/search_response.py">SearchResponse</a></code>
