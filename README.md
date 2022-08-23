<!-- markdownlint-disable MD033 -->
<h1 align="center">
  Switcher Web API
  <br/>
  <a href="https://hub.docker.com/r/tomerfi/switcher_webapi">
    <img src="https://img.shields.io/docker/v/tomerfi/switcher_webapi?color=%230A6799&logo=docker"/>
  </a>
  <a href="https://hub.docker.com/r/tomerfi/switcher_webapi">
    <img src="https://img.shields.io/docker/pulls/tomerfi/switcher_webapi.svg?logo=docker&label=pulls"/>
  </a>
  <a href="https://codecov.io/gh/TomerFi/switcher_webapi">
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
        <a href="https://github.com/TomerFi/switcher_webapi/blob/dev/.github/CONTRIBUTING.md" target="_blank">
          Contributing Guidelines
        </a>
      </td>
    </tr>
  </table>
</p>

<p align="center">
<strong>Our contributors </strong><a href="https://allcontributors.org/docs/en/emoji-key"><em>emoji keys</em></a>
<br/>
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/dolby360"><img src="https://avatars.githubusercontent.com/u/22151399?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Dolev Ben Aharon</b></sub></a><br /><a href="https://github.com/TomerFi/switcher_webapi/commits?author=dolby360" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/OrBin"><img src="https://avatars.githubusercontent.com/u/6897234?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Or Bin</b></sub></a><br /><a href="https://github.com/TomerFi/switcher_webapi/commits?author=OrBin" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/saar-win"><img src="https://avatars.githubusercontent.com/u/61886120?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Saar wintrov</b></sub></a><br /><a href="https://github.com/TomerFi/switcher_webapi/commits?author=saar-win" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/thecode"><img src="https://avatars.githubusercontent.com/u/1858925?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Shay Levy</b></sub></a><br /><a href="#design-thecode" title="Design">🎨</a> <a href="#userTesting-thecode" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/dmatik"><img src="https://avatars.githubusercontent.com/u/5577386?v=4?s=100" width="100px;" alt=""/><br /><sub><b>dmatik</b></sub></a><br /><a href="#blog-dmatik" title="Blogposts">📝</a> <a href="#ideas-dmatik" title="Ideas, Planning, & Feedback">🤔</a> <a href="#userTesting-dmatik" title="User Testing">📓</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
</p>
