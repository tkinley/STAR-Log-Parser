# RNASeq-Mapping-Summary

A Python script to extract mapping statistics from STAR alignment log files and export them to a CSV file.

## Features

- Extracts number of input reads, uniquely mapped reads number, and uniquely mapped reads percentage.
- Parses STAR log files and consolidates results into a CSV file.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/RNASeq-Mapping-Summary.git
    cd RNASeq-Mapping-Summary
    ```

2. Place your STAR log files in the `log_files` directory.

3. Run the script:
    ```bash
    python extract_mapping_info.py
    ```

4. The results will be saved in `mapping_summary.csv`.

#### Note:
This will create a CSV file named mapping_summary.csv in the same directory, containing the extracted information sorted by filenames in ascending order. If you need to sort in descending order, you can modify the sorted function call to include the reverse=True parameter:
```python
import pandas as pd
data_sorted = sorted(data, key=lambda x: x["Filename"], reverse=True)
```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
