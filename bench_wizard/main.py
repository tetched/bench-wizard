from typing import Optional

import click

from bench_wizard.benchmark import run_pallet_benchmarks
from bench_wizard.config import Config
from bench_wizard.db_bench import run_db_benchmark


@click.group()
def main():
    pass


@main.command("benchmark")
@click.option(
    "--include-db-benchmark",
    type=bool,
    default=False,
    is_flag=True,
    help="Perform Substrate Database benchmark",
)
@click.option(
    "--no-pallet-benchmarks",
    type=bool,
    default=False,
    is_flag=True,
    help="Skip pallets benchmarks",
)
@click.option(
    "--substrate-repo-path",
    type=str,
    default="./substrate",
    help="Substrate repository path (cloned if not provided or does not exist)",
)
@click.option(
    "--reference-values",
    type=str,
    default=".maintain/bench-check/hydradx-bench-data.json",
    help="Reference values - json format",
)
@click.option(
    "--reference-values",
    type=str,
    default=".maintain/bench-check/hydradx-bench-data.json",
    help="Reference values - json format",
)
@click.option("-p", "--pallet", type=str, multiple=True, required=False, help="Pallets")
def benchmark(
    include_db_benchmark: bool,
    no_pallet_benchmarks: bool,
    substrate_repo_path: str,
    reference_values: str,
    pallet: Optional[list],
):
    config = Config(
        do_db_bench=include_db_benchmark,
        substrate_repo_path=substrate_repo_path,
        do_pallet_bench=not no_pallet_benchmarks,
        reference_values=reference_values,
        pallets=pallet,
    )

    run_pallet_benchmarks(config)
    run_db_benchmark(config)