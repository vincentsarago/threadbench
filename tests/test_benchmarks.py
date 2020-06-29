"""Benchmark."""

from concurrent import futures

import mercantile
import pytest
import rasterio
from rio_tiler_crs import COGReader

tile = mercantile.Tile(x=2399, y=1696, z=12)

assets = [
    "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/2019/S2B_36RTT_20191205_0_L2A/TCI.tif",
    "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/2019/S2A_36RTT_20191203_0_L2A/TCI.tif",
    "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/2019/S2B_36RTT_20191128_0_L2A/TCI.tif",
    "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/2019/S2A_36RTT_20191123_0_L2A/TCI.tif",
    "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/2019/S2A_36RTT_20191120_0_L2A/TCI.tif",
    "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/2019/S2B_36RTT_20191118_0_L2A/TCI.tif",
    "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/2019/S2A_36RTT_20191113_0_L2A/TCI.tif",
    "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/2019/S2B_36RTT_20191105_0_L2A/TCI.tif",
    "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/2019/S2A_36RTT_20191103_0_L2A/TCI.tif",
    "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/2019/S2B_36RTT_20191029_0_L2A/TCI.tif",
]


def _tiler(asset):
    with COGReader(asset) as cog:
        cog.tile(*tile)
    return True


def read_tile(nb_images, threads):
    """Benchmark rio-tiler.utils._tile_read."""

    test_assets = assets[:nb_images]

    with rasterio.Env(
        GDAL_CACHEMAX=0,
        VSI_CACHE="FALSE",
        VSI_CACHE_SIZE=0,
        NUM_THREADS="all",
        CPL_VSIL_CURL_NON_CACHED="/vsicurl/https://sentinel",
        GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR",
    ):
        if not threads:
            for asset in test_assets:
                _tiler(asset)
        else:
            with futures.ThreadPoolExecutor(max_workers=threads) as executor:
                [executor.submit(_tiler, asset) for asset in test_assets]

    return True


@pytest.mark.parametrize("threads", [0, 1, 2, 5, 10])
@pytest.mark.parametrize("nb_images", [1, 2, 5, 10])
def test_tile(benchmark, nb_images, threads):
    """Test tile read for multiple combination of datatype/mask/tile extent."""
    benchmark.name = f"{nb_images}images-{threads}threads"
    benchmark.group = f"{nb_images}images"
    _ = benchmark(read_tile, nb_images, threads)
