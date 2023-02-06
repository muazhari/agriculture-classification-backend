import pytest
from fastapi.encoders import jsonable_encoder

from app.inner.models.entities.classification import Process
from app.outer.interfaces.gateways.BaseClient import BaseClient
from app.outer.repositories import classification_repository

mock_data: [Process] = [
    Process(id='6d2bcb36-ae72-4270-bc36-0a45deb9d710', title="title 0", description="description 0"),
    Process(id='6d2bcb36-ae72-4270-bc36-0a45deb9d711', title="title 1", description="description 1"),
]

client = BaseClient(
    base_url="http://localhost:8000"
)


async def do_before_each_tests():
    global mock_data
    for index, entity in enumerate(mock_data):
        print(index, entity)
        created_entity = tutorial_repository.create_one(entity)


async def do_after_each_tests():
    global mock_data
    for index, entity in enumerate(mock_data):
        print(index, entity)
        deleted_entity = tutorial_repository.delete_one_by_id(entity.id)


@pytest.mark.asyncio
@pytest.fixture(scope="module", autouse=True)
async def run_around_tests():
    print("1")
    await do_before_each_tests()
    print("2")
    yield
    print("3")
    await do_after_each_tests()
    print("4")


# read all test
@pytest.mark.asyncio
async def test_read_all(run_around_tests):
    global mock_data, client
    session = await client.get_client_session()
    async with session.get(f"/api/tutorial") as response:
        assert response.status == 200
        entities = [Process(**entity) for entity in await response.json()]
        assert all([entity in entities for entity in mock_data])


# read one by id test
@pytest.mark.asyncio
async def test_read_one_by_id():
    global mock_data, client
    mock_entity = mock_data[0]
    session = await client.get_client_session()
    async with session.get(f"/api/tutorial/{mock_entity.id}") as response:
        assert response.status == 200
        entity = Process(**await response.json())
        assert entity == mock_entity


# create one test
@pytest.mark.asyncio
async def test_create_one():
    global mock_data, client
    mock_entity = Process(id='6d2bcb36-ae72-4270-bc36-0a45deb9d712', title="title 2", description="description 2")
    session = await client.get_client_session()
    with session.post(f"/api/tutorial", data=mock_entity.dict()) as response:
        assert response.status == 200
        entity = Process(**await response.json())
        assert entity == mock_entity


# patch one by id test
@pytest.mark.asyncio
async def test_patch_one_by_id():
    global mock_data, client
    mock_entity = mock_data[0]
    mock_entity.title = "new title"
    mock_entity.description = "new description"
    session = await client.get_client_session()
    with session.patch(f"/api/tutorial/{mock_entity.id}", data=mock_entity.dict()) as response:
        assert response.status == 200
        entity = Process(**await response.json())
        assert entity == mock_entity


# delete one by id test
@pytest.mark.asyncio
async def test_delete_one_by_id():
    global mock_data, client
    mock_entity = mock_data[0]
    session = await client.get_client_session()
    with session.delete(f"/api/tutorial/{mock_entity.id}") as response:
        assert response.status == 200
        entity = Process(**await response.json())
        assert entity == mock_entity
