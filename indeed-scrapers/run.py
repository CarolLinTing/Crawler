# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:43:45 2024

@author: user
"""

"""
This sample code is from the SCRAPFLY git(https://github.com/scrapfly)
This example run script shows how to run the Indeed.com scraper defined in ./indeed.py
It scrapes hotel data and saves it to ./results/

To run this script set the env variable $SCRAPFLY_KEY with your scrapfly API key:
$ export $SCRAPFLY_KEY="your key from https://scrapfly.io/dashboard"
"""
import asyncio
import json
from pathlib import Path
import indeed
# 导入 transferExcel.py 中的函数
from transferExcel import json_to_excel

output = Path(__file__).parent / "results"
output.mkdir(exist_ok=True)


async def run():
    # enable scrapfly cache for basic use
    indeed.BASE_CONFIG["cache"] = True

    print("running Indeed scrape and saving results to ./results directory")

    #url = "https://www.indeed.com/jobs?q=python&l=Texas"
    url = "https://uk.indeed.com/jobs?q=&l=Sheffield%2C+South+Yorkshire&vjk=e525df493a1ef7f8"
    result_search = await indeed.scrape_search(url, max_results=100)
    output.joinpath("search.json").write_text(json.dumps(result_search, indent=2, ensure_ascii=False), encoding='utf-8')
    jobs = ["4c1e2988b22fa223", "483d39cbe1b6c1fe"]
    result_jobs = await indeed.scrape_jobs(jobs)
    output.joinpath("jobs.json").write_text(json.dumps(result_jobs, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    #asyncio.run(run())
    asyncio.create_task(run())
    
# transfer the output JSON to excel file
print("Start transfer")
json_file_path = 'C:/Users/user/Desktop/工作/工作爬蟲/indeed-scrapers/results/search.json'
excel_file_path = 'jobSearchResult.xlsx'                 # excel name
print("haaaaa")

json_to_excel(json_file_path, excel_file_path)
