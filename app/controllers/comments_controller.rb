class CommentsController < ApplicationController
    before_action :set_post
    def create
        comment_params
        # Create associated model, just like we did in the console before
        @comment = @post.comments.create(comment_params).permit(:content)
        # We want to show the comment in the context of the Post
        redirect_to post_path(@post)
    end


    def update
        set_comment
        @comment.update(comment_params)
        redirect_to @post
    end

    def destroy
        set_comment
        @comment.destroy
        redirect_to @post
    end

    private
    def comment_params
        params.require(:comment).permit(:content)
    end

    def set_post
        @post = Post.find(params[:post_id])
    end

    def set_comment
        @comment = Comment.find(params[:id])
    end
end
