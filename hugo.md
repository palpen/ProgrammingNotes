# Notes on Hugo

https://gohugo.io/

# Commands
Create new post (run inside root dir of site): `hugo new posts/new-post.md`

Start Hugo server: `hugo server -D`

# Notes

* How to enable HTML tags in Hugo (when default markdown engine is goldmark). This is useful for resizing images in your posts by using `<img src="/img/myimg.png" width="1000"/>`

    * In the `config.toml` file, add
    ```
    [markup]
        defaultMarkdownHandler = "goldmark"
        [markup.goldmark]
            [markup.goldmark.renderer]
                unsafe = true
    ```

    * Alternatively, one can set the markdown engine back to blackfriday (change "goldmark" to "blackfriday" above)

    * see https://jdhao.github.io/2019/12/29/hugo_html_not_shown/
