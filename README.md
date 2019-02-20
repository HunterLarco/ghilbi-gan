# GhibliGAN

A style-transfer project using [CycleGAN] to render photos in the style of
Studio Ghibli animations.

> Note that this project is built as a learning project for myself and that if
> you're looking for a tried-and-true implementation of CycleGAN you should 
> refer to their [original PyTorch source][CycleGANSource] or look at one of the
> several [Tensorflow adaptations][CycleGANTensorflow].

## Build Setup

```bash
# install package manager
pip install pipenv

# install dependencies
pipenv install
```

## Code Quality

```bash
# get linter aggregate statistics
pipenv run pycodestyle --statistics -qq --config pycodestyle.cfg src

# lint a specific file(s)
pipenv run pycodestyle --first --show-source --config pycodestyle.cfg <file>
```

## Model Architecture

The base for this model is [CycleGAN]&mdash;the generator network follows
[Johnson et al.] while the discriminator follows [PatchGAN].

[CycleGAN]: https://arxiv.org/abs/1703.10593
[CycleGANSource]: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
[CycleGANTensorflow]: https://github.com/search?q=CycleGan+tensorflow
[Johnson et al.]: https://arxiv.org/abs/1603.08155
[PatchGAN]: https://arxiv.org/abs/1611.07004
