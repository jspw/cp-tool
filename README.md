# cp-tool

![](https://img.shields.io/badge/version-2.1.1-blue) ![](https://img.shields.io/badge/license-MIT-brightgreen)

**cp-tool** is an auto generator for solved problems at different online judges. It gathers all the problems you have solved at an online judge and generates a git repository for you.

Generated [Sample Git Rep](https://github.com/jspw/cp-tool-sample) by [cp-tool](https://github.com/jspw/cp-tool)

## Supported Platforms

- [Codeforces](https://codeforces.com)

## Requirments

- python >=3.6

## Instruction

- ### Installation

  - Linux :

  >     pip install cp-tool

  - Windows :

  >     python -m pip install cp-tool

**Note : Please updated version**

- ### Upgrade :

  - Linux :

  > pip install --upgrade cp-tool

  - Windows :

  > python -m pip install --upgrade cp-tool

- ### Usage

  - Using command `cp-tool` it will show the usages

    ![](https://dev-to-uploads.s3.amazonaws.com/i/hu6au7bfw4f44mwemoca.png)

  - Init with git repo :

    - Create a git repository first
    - Then init

      >     cp-tool -c init -j codeforces

      You will be asked for

      - handle

        - example : `shifat57`

      - repository name (A folder will be created based in repo name)

        - example : `My Cp Track`

      - repository url
        - example : `https://github.com/jspw/cp-tool-sample`

      ![](https://dev-to-uploads.s3.amazonaws.com/i/s7ja0xgwrft0r5oq4k51.png)

  - Update submissions :

    - Go to the repository folder in your local file

    - Then

      > cp-tool -c update -j codeforces

    ![](https://dev-to-uploads.s3.amazonaws.com/i/zl4k70i4cqm6ovcweh6w.png)

## License

[MIT](LICENSE)
