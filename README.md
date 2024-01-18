<h1 align="center">
  Switcher Web API
  <br/>
  <a href="https://hub.docker.com/r/tomerfi/switcher_webapi">
    <img src="https://img.shields.io/docker/v/tomerfi/switcher_webapi?color=%230A6799&logo=docker"/>
  </a>
  <a href="https://hub.docker.com/r/tomerfi/switcher_webapi">
    <img src="https://img.shields.io/docker/pulls/tomerfi/switcher_webapi.svg?logo=docker&label=pulls"/>
  </a>
  <a href="https://github.com/TomerFi/switcher_webapi/blob/dev/LICENSE">
    <img src="https://img.shields.io/github/license/tomerfi/switcher_webapi"/>
  </a>
  <br/>
  <a href="https://github.com/TomerFi/switcher_webapi/actions/workflows/stage.yml">
    <img src="https://github.com/TomerFi/switcher_webapi/actions/workflows/stage.yml/badge.svg"/>
  </a>
  <a href="https://github.com/TomerFi/switcher_webapi/actions/workflows/pages.yml">
    <img src="https://github.com/TomerFi/switcher_webapi/actions/workflows/pages.yml/badge.svg"/>
  </a>
  <a href="https://codecov.io/gh/TomerFi/switcher_webapi">
    <img src="https://codecov.io/gh/TomerFi/switcher_webapi/graph/badge.svg"/>
  </a>
</h1>

<h3 align="center">
  Gain containerized access to your local <a href="https://www.switcher.co.il/">Switcher</a> smart devices
</h3>
<p align="center">

  ```mermaid
  flowchart LR
    A([User]) -- HTTP --> B([Container]) -- TCP --> C([Device])
  ```

  ```shell
  docker run -d -p 8000:8000 --name switcher_webapi tomerfi/switcher_webapi:latest
  ```

</p>

<p align="center">
  <table align="center">
    <tr>
      <td align="left">
        <a href="https://switcher-webapi.tomfi.info" target="_blank">Read Docs</a>
      </td>
      <td align="left">
        <a href="https://github.com/TomerFi/switcher_webapi/wiki" target="_blank">Wiki Pages</a>
      </td>
      <td align="left">
        <a href="https://github.com/TomerFi/switcher_webapi/blob/dev/.github/CODE_OF_CONDUCT.md" target="_blank">
          Code of Conduct
        </a>
      </td>
    </tr>
    <tr>
      <td align="left" colspan="2">
        <a href="https://github.com/TomerFi/aioswitcher/wiki" target="_blank">
          <em>aioswitcher</em>'s Wiki Pages
        </a>
      </td>
      <td align="left">
        <a href="https://github.com/TomerFi/switcher_webapi/blob/dev/CONTRIBUTING.md" target="_blank">
          Contributing Guidelines
        </a>
      </td>
    </tr>
  </table>
</p>

<p align="center">
<strong>Our contributors </strong><a href="https://allcontributors.org/docs/en/emoji-key"><em>emoji keys</em></a><br/>
<img alt="all-contributors" src="https://img.shields.io/github/all-contributors/tomerfi/switcher_webapi?color=ee8449&style=flat-square">
<br/>
<div align="center">
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dolby360"><img src="https://avatars.githubusercontent.com/u/22151399?v=4?s=100" width="100px;" alt="Dolev Ben Aharon"/><br /><sub><b>Dolev Ben Aharon</b></sub></a><br /><a href="https://github.com/TomerFi/switcher_webapi/commits?author=dolby360" title="Documentation">📖</a> <a href="https://github.com/TomerFi/switcher_webapi/commits?author=dolby360" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://altmascinco.wordpress.com"><img src="https://avatars.githubusercontent.com/u/1054618?v=4?s=100" width="100px;" alt="Jorge Vallecillo"/><br /><sub><b>Jorge Vallecillo</b></sub></a><br /><a href="#infra-altmas5" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/OrBin"><img src="https://avatars.githubusercontent.com/u/6897234?v=4?s=100" width="100px;" alt="Or Bin"/><br /><sub><b>Or Bin</b></sub></a><br /><a href="https://github.com/TomerFi/switcher_webapi/commits?author=OrBin" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/saar-win"><img src="https://avatars.githubusercontent.com/u/61886120?v=4?s=100" width="100px;" alt="Saar wintrov"/><br /><sub><b>Saar wintrov</b></sub></a><br /><a href="https://github.com/TomerFi/switcher_webapi/commits?author=saar-win" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/thecode"><img src="https://avatars.githubusercontent.com/u/1858925?v=4?s=100" width="100px;" alt="Shay Levy"/><br /><sub><b>Shay Levy</b></sub></a><br /><a href="#design-thecode" title="Design">🎨</a> <a href="#userTesting-thecode" title="User Testing">📓</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/YogevBokobza"><img src="https://avatars.githubusercontent.com/u/22839127?v=4?s=100" width="100px;" alt="YogevBokobza"/><br /><sub><b>YogevBokobza</b></sub></a><br /><a href="https://github.com/TomerFi/switcher_webapi/commits?author=YogevBokobza" title="Code">💻</a> <a href="https://github.com/TomerFi/switcher_webapi/commits?author=YogevBokobza" title="Documentation">📖</a> <a href="https://github.com/TomerFi/switcher_webapi/commits?author=YogevBokobza" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dmatik"><img src="https://avatars.githubusercontent.com/u/5577386?v=4?s=100" width="100px;" alt="dmatik"/><br /><sub><b>dmatik</b></sub></a><br /><a href="#blog-dmatik" title="Blogposts">📝</a> <a href="#ideas-dmatik" title="Ideas, Planning, & Feedback">🤔</a> <a href="#userTesting-dmatik" title="User Testing">📓</a> <a href="#maintenance-dmatik" title="Maintenance">🚧</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
</div>
</p>
