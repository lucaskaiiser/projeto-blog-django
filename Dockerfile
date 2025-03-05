FROM archlinux:latest
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
RUN pacman -Syu --noconfirm && pacman -S python --noconfirm
RUN useradd -m -G wheel builder && passwd -d builder
RUN echo "builder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN mkdir /app
WORKDIR /app
RUN chown -R builder:builder . && chmod -R 777 .
USER builder
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="/home/builder/.local/bin:$PATH"
CMD ["poetry", "run","python","src/manage.py","runserver", "0.0.0.0:8000"]
