[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Arbre de compétences</h3>

<p align="center">
  Web app that helps easily store and analyze in a graphical way skills from Simplon students.
  <a href="https://gauthierginier.github.io/adc-heroku/"><strong>Explore the docs »</strong></a>
  <br />
  <br />
  <a href="https://github.com/gauthierginier/adc-heroku">View Demo</a>
  ·
  <a href="https://github.com/gauthierginier/adc-heroku/issues">Report Bug</a>
  ·
  <a href="https://github.com/gauthierginier/adc-heroku/issues">Request Feature</a>
</p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

<div style='display:flex;'>
  <img src="https://media.giphy.com/media/xUA7b2OfgTuVzqpVXq/giphy.gif" width="60" height="60" />
</div>


### Built With

- []()Heroku
- []()Docker
- []()Pytest
- []()Postgresql
- []()SqlAlchemy
- []()Python
- []()Flask
- []()UWSGI
- []()Bulma
- []()Chartjs
- []()Javascript
- []()YML
- []()Sphinx

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Python
  ```sh
  python version 3.6 or greater.
  ```

### Directory structure
```sh
  .
├── app
│   ├── auth
│   │   └── templates
│   ├── dashboard
│   │   └── templates
│   ├── static
│   └── templates
├── docs
│   ├── build
│   │   ├── doctrees
│   │   └── html
│   │       ├── _sources
│   │       └── _static
│   │           ├── css
│   │           └── img
│   └── source
│       ├── _static
│       └── _templates
└── tests
    └── dashboard_views

20 directories

```

### Installation

1. Clone the repo
   ```sh
   $ git clone https://github.com/gauthierginier/adc-heroku
   ```
2. Create & activate virtual environment
   ```sh
   $ python -m venv .venv
   ```
   ```sh
   $ source .venv/bin/activate
   ```
3. Install requirements.txt packages
   ```sh
   $ python install -r requirements.txt
   ```

<!-- USAGE EXAMPLES -->

## Usage

### Tests

1. Create environnement variables. If you run flask application locally varibles will be recreated.
  ```sh
  $ export FLASK_SECRET_KEY=lol
  ```
  ```sh
  $ export DATABASE_URL2=sqlite:///db.sqlite
  ```
2. Run tests from root directory
  ```sh
  $ python -m pytest -v
  ```

### Run flask application locally

1. From root directory run:
  ```sh
  $ ./launch.sh
  ```

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/gauthierginier/adc-heroku/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Gauthier Ginier, Adrian Ruiz, Nicolas Prodhomme et Abdul

Project Link: [https://github.com/gauthierginier/adc-heroku](https://github.com/gauthierginier/adc-heroku)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- []()Romain
- []()Lumy
- []()Elodie

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/cloud-native-lib/cloud-native-library.svg?style=for-the-badge
[contributors-url]: https://github.com/gauthierginier/adc-heroku/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/cloud-native-lib/cloud-native-library.svg?style=for-the-badge
[forks-url]: https://github.com/gauthierginier/adc-heroku/network/members
[stars-shield]: https://img.shields.io/github/stars/cloud-native-lib/cloud-native-library.svg?style=for-the-badge
[stars-url]: https://github.com/gauthierginier/adc-heroku/stargazers
[issues-shield]: https://img.shields.io/github/issues/cloud-native-lib/cloud-native-library.svg?style=for-the-badge
[issues-url]: https://github.com/gauthierginier/adc-heroku/issues
[license-shield]: https://img.shields.io/github/license/cloud-native-lib/cloud-native-library.svg?style=for-the-badge
[license-url]: https://github.com/gauthierginier/adc-heroku/blob/main/LICENSE.txt
