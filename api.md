# Embeddings

Types:

```python
from taam_cloud.types import EmbeddingCreateResponse
```

Methods:

- <code title="post /v1/embeddings">client.embeddings.<a href="./src/taam_cloud/resources/embeddings.py">create</a>(\*\*<a href="src/taam_cloud/types/embedding_create_params.py">params</a>) -> <a href="./src/taam_cloud/types/embedding_create_response.py">object</a></code>

# Rerank

Methods:

- <code title="post /v1/rerank">client.rerank.<a href="./src/taam_cloud/resources/rerank.py">create</a>(\*\*<a href="src/taam_cloud/types/rerank_create_params.py">params</a>) -> None</code>

# Chat

Methods:

- <code title="post /v1/chat/completions">client.chat.<a href="./src/taam_cloud/resources/chat.py">create_completion</a>(\*\*<a href="src/taam_cloud/types/chat_create_completion_params.py">params</a>) -> None</code>

# Suno

## Submit

Methods:

- <code title="post /suno/submit/music">client.suno.submit.<a href="./src/taam_cloud/resources/suno/submit.py">generate_music</a>(\*\*<a href="src/taam_cloud/types/suno/submit_generate_music_params.py">params</a>) -> None</code>

# Models

Types:

```python
from taam_cloud.types import ModelListResponse
```

Methods:

- <code title="get /v1/models">client.models.<a href="./src/taam_cloud/resources/models.py">list</a>() -> <a href="./src/taam_cloud/types/model_list_response.py">ModelListResponse</a></code>

# Images

Types:

```python
from taam_cloud.types import ImageGenerateResponse
```

Methods:

- <code title="post /v1/images/generations">client.images.<a href="./src/taam_cloud/resources/images.py">generate</a>(\*\*<a href="src/taam_cloud/types/image_generate_params.py">params</a>) -> <a href="./src/taam_cloud/types/image_generate_response.py">ImageGenerateResponse</a></code>

# Web

Types:

```python
from taam_cloud.types import WebCreateResponse
```

Methods:

- <code title="post /v1/web">client.web.<a href="./src/taam_cloud/resources/web.py">create</a>(\*\*<a href="src/taam_cloud/types/web_create_params.py">params</a>) -> <a href="./src/taam_cloud/types/web_create_response.py">WebCreateResponse</a></code>

# Files

Types:

```python
from taam_cloud.types import FileRetrieveResponse, FileUploadResponse
```

Methods:

- <code title="get /v1/files/retrieve">client.files.<a href="./src/taam_cloud/resources/files.py">retrieve</a>(\*\*<a href="src/taam_cloud/types/file_retrieve_params.py">params</a>) -> <a href="./src/taam_cloud/types/file_retrieve_response.py">FileRetrieveResponse</a></code>
- <code title="post /v1/files">client.files.<a href="./src/taam_cloud/resources/files.py">upload</a>(\*\*<a href="src/taam_cloud/types/file_upload_params.py">params</a>) -> <a href="./src/taam_cloud/types/file_upload_response.py">FileUploadResponse</a></code>

# Upload

Types:

```python
from taam_cloud.types import UploadCreateResponse
```

Methods:

- <code title="post /upload">client.upload.<a href="./src/taam_cloud/resources/upload.py">create</a>(\*\*<a href="src/taam_cloud/types/upload_create_params.py">params</a>) -> <a href="./src/taam_cloud/types/upload_create_response.py">UploadCreateResponse</a></code>

# VideoGeneration

Types:

```python
from taam_cloud.types import VideoGenerationCreateResponse
```

Methods:

- <code title="post /v1/video_generation">client.video_generation.<a href="./src/taam_cloud/resources/video_generation.py">create</a>(\*\*<a href="src/taam_cloud/types/video_generation_create_params.py">params</a>) -> <a href="./src/taam_cloud/types/video_generation_create_response.py">VideoGenerationCreateResponse</a></code>

# Query

Types:

```python
from taam_cloud.types import QueryCheckVideoGenerationStatusResponse
```

Methods:

- <code title="get /v1/query/video_generation">client.query.<a href="./src/taam_cloud/resources/query.py">check_video_generation_status</a>(\*\*<a href="src/taam_cloud/types/query_check_video_generation_status_params.py">params</a>) -> <a href="./src/taam_cloud/types/query_check_video_generation_status_response.py">QueryCheckVideoGenerationStatusResponse</a></code>
