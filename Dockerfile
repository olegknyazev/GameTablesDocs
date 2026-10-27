FROM jekyll/jekyll:4.2.0@sha256:de110e0fdde342de0cb6fd5c63f64934b6ce25d0dd826c67113b3a5a3370784e
COPY Gemfile Gemfile.lock ./
RUN bundle install
