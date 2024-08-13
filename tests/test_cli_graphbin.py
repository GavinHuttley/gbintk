import pathlib
import pytest

from click.testing import CliRunner

from gbintk.cli import graphbin


__author__ = "Vijini Mallawaarachchi"
__credits__ = ["Vijini Mallawaarachchi"]


DATADIR = pathlib.Path(__file__).parent / "data"

@pytest.fixture(scope="session")
def tmp_dir(tmpdir_factory):
    return tmpdir_factory.mktemp("tmp")


@pytest.fixture(autouse=True)
def workingdir(tmp_dir, monkeypatch):
    """set the working directory for all tests"""
    monkeypatch.chdir(tmp_dir)


@pytest.fixture(scope="session")
def runner():
    """exportrc works correctly."""
    return CliRunner()


def test_graphbin_run(runner, tmp_dir):
    outpath = tmp_dir
    graph = DATADIR / "ESC_metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    contigs = DATADIR / "ESC_metaSPAdes" / "contigs.fasta"
    paths = DATADIR / "ESC_metaSPAdes" / "contigs.paths"
    binned = DATADIR / "ESC_metaSPAdes" / "initial_binning_res.csv"
    args = f"--assembler spades --graph {graph} --contigs {contigs} --paths {paths} --binned {binned} --output {outpath}".split()
    r = runner.invoke(graphbin, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output
