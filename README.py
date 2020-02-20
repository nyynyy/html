<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:css='false' b:defaultwidgetversion='2' b:layoutsVersion='3' b:responsive='true' b:templateUrl='fancy.xml' b:templateVersion='1.3.0' expr:dir='data:blog.languageDirection' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
  <head>
    <meta content='width=device-width, initial-scale=1' name='viewport'/>
    <title><data:view.title.escaped/></title>
    <b:include data='blog' name='all-head-content'/>
    <b:skin version='1.3.0'><![CDATA[/*! normalize.css v3.0.1 | MIT License | git.io/normalize */html{font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}body{margin:0}article,aside,details,figcaption,figure,footer,header,hgroup,main,nav,section,summary{display:block}audio,canvas,progress,video{display:inline-block;vertical-align:baseline}audio:not([controls]){display:none;height:0}[hidden],template{display:none}a{background:transparent}a:active,a:hover{outline:0}abbr[title]{border-bottom:1px dotted}b,strong{font-weight:bold}dfn{font-style:italic}h1{font-size:2em;margin:.67em 0}mark{background:#ff0;color:#000}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sup{top:-0.5em}sub{bottom:-0.25em}img{border:0}svg:not(:root){overflow:hidden}figure{margin:1em 40px}hr{-moz-box-sizing:content-box;box-sizing:content-box;height:0}pre{overflow:auto}code,kbd,pre,samp{font-family:monospace,monospace;font-size:1em}button,input,optgroup,select,textarea{color:inherit;font:inherit;margin:0}button{overflow:visible}button,select{text-transform:none}button,html input[type="button"],input[type="reset"],input[type="submit"]{-webkit-appearance:button;cursor:pointer}button[disabled],html input[disabled]{cursor:default}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0}input{line-height:normal}input[type="checkbox"],input[type="radio"]{box-sizing:border-box;padding:0}input[type="number"]::-webkit-inner-spin-button,input[type="number"]::-webkit-outer-spin-button{height:auto}input[type="search"]{-webkit-appearance:textfield;-moz-box-sizing:content-box;-webkit-box-sizing:content-box;box-sizing:content-box}input[type="search"]::-webkit-search-cancel-button,input[type="search"]::-webkit-search-decoration{-webkit-appearance:none}fieldset{border:1px solid #c0c0c0;margin:0 2px;padding:.35em .625em .75em}legend{border:0;padding:0}textarea{overflow:auto}optgroup{font-weight:bold}table{border-collapse:collapse;border-spacing:0}td,th{padding:0}
/*
<!-- Constants -->

<!-- Fonts -->

<Variable name="garamond12" description="12px Garamond" type="font" default="normal 400 12px EB Garamond, serif" hideEditor="true"  value="normal 400 12px EB Garamond, serif"/>
<Variable name="garamond14" description="14px Garamond" type="font" default="normal 400 14px EB Garamond, serif" hideEditor="true"  value="normal 400 14px EB Garamond, serif"/>
<Variable name="garamond16" description="16px Garamond" type="font" default="normal 400 16px EB Garamond, serif" hideEditor="true"  value="normal 400 16px EB Garamond, serif"/>
<Variable name="garamond18" description="18px Garamond" type="font" default="normal 400 18px EB Garamond, serif" hideEditor="true"  value="normal 400 18px EB Garamond, serif"/>
<Variable name="garamond20" description="20px Garamond" type="font" default="normal 400 20px EB Garamond, serif" hideEditor="true"  value="normal 400 20px EB Garamond, serif"/>
<Variable name="garamond24" description="24px Garamond" type="font" default="normal 400 24px EB Garamond, serif" hideEditor="true"  value="normal 400 24px EB Garamond, serif"/>
<Variable name="garamond36" description="36px Garamond" type="font" default="normal 400 36px EB Garamond, serif" hideEditor="true"  value="normal 400 36px EB Garamond, serif"/>
<Variable name="lato12" description="12px Lato" type="font" default="normal 400 12px Lato, sans-serif" hideEditor="true"  value="normal 400 12px Lato, sans-serif"/>
<Variable name="lato14" description="14px Lato" type="font" default="normal 400 14px Lato, sans-serif" hideEditor="true"  value="normal 400 14px Lato, sans-serif"/>
<Variable name="lato16" description="16px Lato" type="font" default="normal 400 16px Lato, sans-serif" hideEditor="true"  value="normal 400 16px Lato, sans-serif"/>
<Variable name="lato20" description="20px Lato" type="font" default="normal 400 20px Lato, sans-serif" hideEditor="true"  value="normal 400 20px Lato, sans-serif"/>
<Variable name="lato24" description="24px Lato" type="font" default="normal 400 24px Lato, sans-serif" hideEditor="true"  value="normal 400 24px Lato, sans-serif"/>
<Variable name="latoBold12" description="12px Lato Bold" type="font" default="normal 700 12px Lato, sans-serif" hideEditor="true"  value="normal 700 12px Lato, sans-serif"/>
<Variable name="latoBold14" description="14px Lato Bold" type="font" default="normal 700 14px Lato, sans-serif" hideEditor="true"  value="normal 700 14px Lato, sans-serif"/>
<Variable name="latoBold16" description="16px Lato Bold" type="font" default="normal 700 16px Lato, sans-serif" hideEditor="true"  value="normal 700 16px Lato, sans-serif"/>
<Variable name="latoBold24" description="24px Lato Bold" type="font" default="normal 700 24px Lato, sans-serif" hideEditor="true"  value="normal 700 24px Lato, sans-serif"/>
<Variable name="latoBold28" description="28px Lato Bold" type="font" default="normal 700 28px Lato, sans-serif" hideEditor="true"  value="normal 700 28px Lato, sans-serif"/>
<Variable name="latoLight18" description="18px Lato Light" type="font" default="normal 300 18px Lato, sans-serif" hideEditor="true"  value="normal 300 18px Lato, sans-serif"/>
<Variable name="latoLight20" description="20px Lato Light" type="font" default="normal 300 20px Lato, sans-serif" hideEditor="true"  value="normal 300 20px Lato, sans-serif"/>
<Variable name="latoLight24" description="24px Lato Light" type="font" default="normal 300 24px Lato, sans-serif" hideEditor="true"  value="normal 300 24px Lato, sans-serif"/>
<Variable name="latoLight36" description="36px Lato Light" type="font" default="normal 300 36px Lato, sans-serif" hideEditor="true"  value="normal 300 36px Lato, sans-serif"/>
<Variable name="lora14" description="14px Lora" type="font" default="normal 400 14px Lora, serif" hideEditor="true"  value="normal 400 14px Lora, serif"/>
<Variable name="lora16" description="16px Lora" type="font" default="normal 400 16px Lora, serif" hideEditor="true"  value="normal 400 16px Lora, serif"/>
<Variable name="montserrat12" description="12px Montserrat" type="font" default="normal 400 12px Montserrat, sans-serif" hideEditor="true"  value="normal 400 12px Montserrat, sans-serif"/>
<Variable name="montserrat14" description="14px Montserrat" type="font" default="normal 400 14px Montserrat, sans-serif" hideEditor="true"  value="normal 400 14px Montserrat, sans-serif"/>
<Variable name="montserrat16" description="16px Montserrat" type="font" default="normal 400 16px Montserrat, sans-serif" hideEditor="true"  value="normal 400 16px Montserrat, sans-serif"/>
<Variable name="montserrat24" description="24px Montserrat" type="font" default="normal 400 24px Montserrat, sans-serif" hideEditor="true"  value="normal 400 24px Montserrat, sans-serif"/>
<Variable name="montserratBold12" description="12px Montserrat Bold" type="font" default="normal 700 12px Montserrat, sans-serif" hideEditor="true"  value="normal 700 12px Montserrat, sans-serif"/>
<Variable name="montserratBold14" description="14px Montserrat Bold" type="font" default="normal 700 14px Montserrat, sans-serif" hideEditor="true"  value="normal 700 14px Montserrat, sans-serif"/>

<!-- Colors -->

<Variable name="shadowColor" description="Shadow color" type="color" default="rgba(0, 0, 0, 0.1)" hideEditor="true"  value="rgba(0, 0, 0, 0.1)"/>

<!-- Variable definitions -->

<Variable name="keycolor" description="Main Color" type="color" default="#bf8b38"  value="#77e4ff"/>
<Variable name="startSide" description="Start side in blog language" type="automatic" default="left" hideEditor="true" />
<Variable name="endSide" description="End side in blog language" type="automatic" default="right" hideEditor="true" />

<Group description="Body">
  <Variable name="body.background" description="Background" type="background" color="$(body.background.color)" default="$(color) none repeat scroll top left"  value="#01050c url(https://themes.googleusercontent.com/image?id=wltVPUckfSK9W7r7g9igwymWBEo331nLn9RtDt0jiRzLWLfYn17ncXNLjzi6gMZd0cE2mcKHh5eh) no-repeat scroll top center /* Credit: Matt Vince (http://www.offset.com/photos/223311) */;"/>
  <Variable name="body.background.color" description="Background color" type="color" default="#fff"  value="#01050c"/>
  <Variable name="body.title.font.small" description="Title font (small)" type="font" default="$(garamond20)"  value="normal 300 20px Lato, sans-serif"/>
  <Variable name="body.title.font.large" description="Title font (large)" type="font" default="$(garamond24)"  value="normal 300 24px Lato, sans-serif"/>
  <Variable name="body.title.color" description="Title color" type="color" default="#000"  value="#ffffff"/>
  <Variable name="body.action.font.small" description="Action font (small)" type="font" default="$(montserrat12)"  value="normal 700 12px Lato, sans-serif"/>
  <Variable name="body.action.font.large" description="Action font (large)" type="font" default="$(montserrat14)"  value="normal 700 14px Lato, sans-serif"/>
  <Variable name="body.action.color" description="Action color" type="color" default="#bf8b38"  value="#77e4ff"/>
  <Variable name="body.text.font" description="Text font" type="font" default="$(garamond20)"  value="normal 400 20px Lato, sans-serif"/>
  <Variable name="body.text.color" description="Text color" type="color" default="#000"  value="#ffffff"/>
  <Variable name="body.link.color" description="Link color" type="color" default="#bf8b38"  value="#77e4ff"/>
  <Variable name="body.widget.title.font.small" description="Gadget title font (small)" type="font" default="$(montserrat12)"  value="normal 700 12px Lato, sans-serif"/>
  <Variable name="body.widget.title.font.large" description="Gadget title font (large)" type="font" default="$(montserrat14)"  value="normal 700 14px Lato, sans-serif"/>
  <Variable name="body.widget.title.color" description="Gadget title color" type="color" default="rgba(0, 0, 0, 0.54)"  value="rgba(255, 255, 255, 0.54)"/>
  <Variable name="body.filter.background.color" description="Filter background color" type="color" default="#302c24"  value="#77e4ff"/>
  <Variable name="body.filter.text.font.small" description="Filter text font (small)" type="font" default="$(montserrat12)"  value="normal 700 12px Lato, sans-serif"/>
  <Variable name="body.filter.text.font.large" description="Filter text font (large)" type="font" default="$(montserrat14)"  value="normal 700 14px Lato, sans-serif"/>
  <Variable name="body.filter.text.color" description="Filter text color" type="color" default="rgba(255, 255, 255, 0.54)"  value="rgba(0, 0, 0, 0.54)"/>
  <Variable name="body.filter.keyword.font.small" description="Filter keyword font (small)" type="font" default="$(montserratBold12)"  value="normal 700 12px Lato, sans-serif"/>
  <Variable name="body.filter.keyword.font.large" description="Filter keyword font (large)" type="font" default="$(montserratBold14)"  value="normal 700 14px Lato, sans-serif"/>
  <Variable name="body.filter.keyword.color" description="Filter keyword color" type="color" default="rgba(255, 255, 255, 0.87)"  value="rgba(0, 0, 0, 0.87)"/>
  <Variable name="body.filter.link.font.small" description="Filter link font (small)" type="font" default="$(montserratBold12)"  value="normal 700 12px Lato, sans-serif"/>
  <Variable name="body.filter.link.font.large" description="Filter link font (large)" type="font" default="$(montserratBold14)"  value="normal 700 14px Lato, sans-serif"/>
  <Variable name="body.filter.link.color" description="Filter link color" type="color" default="#bf8b38"  value="rgba(0, 0, 0, 0.87)"/>
</Group>

<Group description="Header">
  <Variable name="header.background.color" description="Background color" type="color" default="#fff"  value="#01050c"/>
  <Variable name="header.title.font.small" description="Title font (small)" type="font" default="$(garamond18)"  value="normal 300 18px Lato, sans-serif"/>
  <Variable name="header.title.font.large" description="Title font (large)" type="font" default="$(garamond36)"  value="normal 300 36px Lato, sans-serif"/>
  <Variable name="header.title.color" description="Title color" type="color" default="#000"  value="#ffffff"/>
  <Variable name="header.text.font" description="Text font" type="font" default="$(montserrat12)"  value="normal 400 12px Lato, sans-serif"/>
  <Variable name="header.text.color" description="Text color" type="color" default="rgba(0, 0, 0, 0.54)"  value="rgba(255, 255, 255, 0.54)"/>
  <Variable name="header.pageList.font" description="Page list font" type="font" default="$(montserrat14)"  value="normal 700 14px Lato, sans-serif"/>
  <Variable name="header.pageList.color" description="Page list color" type="color" default="rgba(0, 0, 0, 0.54)"  value="rgba(255, 255, 255, 0.54)"/>
  <Variable name="header.pageList.selected.font" description="Page list font (selected page)" type="font" default="$(montserratBold14)"  value="normal 700 14px Lato, sans-serif"/>
  <Variable name="header.pageList.selected.color" description="Page list color (selected page)" type="color" default="rgba(0, 0, 0, 0.54)"  value="rgba(255, 255, 255, 0.54)"/>
  <Variable name="header.icon.color" description="Icon color" type="color" default="rgba(0, 0, 0, 0.54)"  value="rgba(255, 255, 255, 0.54)"/>
</Group>

<Group description="Posts">
  <Variable name="post.text.background.color" description="Background color (text-only post)" type="color" default="#302c24"  value="#77e4ff"/>
  <Variable name="post.title.font.small" description="Title font (small)" type="font" default="$(garamond20)"  value="normal 400 20px Lato, sans-serif"/>
  <Variable name="post.title.font.large" description="Title font (large)" type="font" default="$(garamond24)"  value="normal 400 24px Lato, sans-serif"/>
  <Variable name="post.title.color" description="Title color" type="color" default="#000"  value="#ffffff"/>
  <Variable name="post.text.title.color" description="Title color (text-only post)" type="color" default="#fff"  value="rgba(0, 0, 0, 0.87)"/>
  <Variable name="post.header.font" description="Header font" type="font" default="$(montserrat12)"  value="normal 700 12px Lato, sans-serif"/>
  <Variable name="post.header.color" description="Header color" type="color" default="rgba(0, 0, 0, 0.54)"  value="rgba(255, 255, 255, 0.54)"/>
  <Variable name="post.text.header.color" description="Header color (text-only post)" type="color" default="rgba(255, 255, 255, 0.54)"  value="rgba(0, 0, 0, 0.54)"/>
  <Variable name="post.footer.font" description="Post Footer Font" type="font" default="$(montserrat12)"  value="normal 700 12px Lato, sans-serif"/>
  <Variable name="post.footer.color" description="Footer color" type="color" default="#bf8b38"  value="#77e4ff"/>
  <Variable name="post.text.font.small" description="Text font (small)" type="font" default="$(lora14)"  value="normal 400 14px Lato, sans-serif"/>
  <Variable name="post.text.font.large" description="Text font (large)" type="font" default="$(lora16)"  value="normal 400 16px Lato, sans-serif"/>
  <Variable name="post.text.color" description="Text color" type="color" default="#000"  value="#ffffff"/>
  <Variable name="post.text.footer.color" description="Footer color (text-only post)" type="color" default="#bf8b38"  value="rgba(0, 0, 0, 0.87)"/>
  <Variable name="post.blockquote.font.small" description="Blockquote font (small)" type="font" default="$(montserrat16)"  value="normal 700 16px Lato, sans-serif"/>
  <Variable name="post.blockquote.font.large" description="Blockquote font (large)" type="font" default="$(montserrat24)"  value="normal 700 24px Lato, sans-serif"/>
  <Variable name="post.blockquote.color" description="Blockquote color" type="color" default="#000"  value="#ffffff"/>
  <Variable name="post.caption.font" description="Caption font" type="font" default="$(montserrat12)"  value="normal 400 16px Lato, sans-serif"/>
  <Variable name="post.caption.color" description="Caption color" type="color" default="#000"  value="#ffffff"/>
</Group>

<Group description="Comments">
  <Variable name="comment.header.font" description="Header font" type="font" default="$(montserrat12)"  value="normal 700 12px Lato, sans-serif"/>
  <Variable name="comment.header.color" description="Header color" type="color" default="rgba(0, 0, 0, 0.54)"  value="rgba(255, 255, 255, 0.54)"/>
  <Variable name="comment.author.font" description="Author font" type="font" default="$(montserrat14)"  value="normal 700 12px Lato, sans-serif"/>
  <Variable name="comment.author.color" description="Author color" type="color" default="#000"  value="#ffffff"/>
  <Variable name="comment.content.font" description="Content font" type="font" default="$(lora14)"  value="normal 400 16px Lato, sans-serif"/>
  <Variable name="comment.content.color" description="Content color" type="color" default="#000"  value="#ffffff"/>
  <Variable name="comment.action.font" description="Action font" type="font" default="$(montserrat12)"  value="normal 700 12px Lato, sans-serif"/>
  <Variable name="comment.action.color" description="Action color" type="color" default="#bf8b38"  value="#77e4ff"/>
</Group>

<Group description="Sidebar">
  <Variable name="sidebar.background.color" description="Background color" type="color" default="#fff"  value="#01050c"/>
  <Variable name="sidebar.separator.color" description="Separator color" type="color" default="rgba(0, 0, 0, 0.54)"  value="rgba(255, 255, 255, 0.54)"/>
  <Variable name="sidebar.profile.name.font" description="Profile name font" type="font" default="$(garamond24)"  value="normal 300 20px Lato, sans-serif"/>
  <Variable name="sidebar.profile.name.color" description="Profile name color" type="color" default="#000"  value="#ffffff"/>
  <Variable name="sidebar.profile.description.font" description="Profile description font" type="font" default="$(montserrat12)"  value="normal 400 12px Lato, sans-serif"/>
  <Variable name="sidebar.profile.description.color" description="Profile description color" type="color" default="rgba(0, 0, 0, 0.87)"  value="rgba(255, 255, 255, 0.87)"/>
  <Variable name="sidebar.action.font" description="Action font" type="font" default="$(montserrat14)"  value="normal 700 14px Lato, sans-serif"/>
  <Variable name="sidebar.action.color" description="Action color" type="color" default="#bf8b38"  value="#77e4ff"/>
  <Variable name="sidebar.widget.title.font" description="Gadget title font" type="font" default="$(montserrat16)"  value="normal 700 16px Lato, sans-serif"/>
  <Variable name="sidebar.widget.title.color" description="Gadget title color" type="color" default="rgba(0, 0, 0, 0.54)"  value="rgba(255, 255, 255, 0.54)"/>
  <Variable name="sidebar.widget.text.font" description="Gadget text font" type="font" default="$(montserrat14)"  value="normal 700 14px Lato, sans-serif"/>
  <Variable name="sidebar.widget.text.color" description="Gadget text color" type="color" default="rgba(0, 0, 0, 0.54)"  value="rgba(255, 255, 255, 0.54)"/>
  <Variable name="sidebar.icon.color" description="Icon color" type="color" default="rgba(0, 0, 0, 0.54)"  value="rgba(255, 255, 255, 0.54)"/>
</Group>

<Group description="Search">
  <Variable name="search.input.font" description="Input font" type="font" default="$(montserrat16)"  value="normal 700 16px Lato, sans-serif"/>
</Group>

<Group description="Sharing">
  <Variable name="sharing.background.color" description="Sharing background color" type="color" default="#fafafa"  value="#252525"/>
  <Variable name="sharing.text.font" description="Sharing text font" type="font" default="$(montserrat16)"  value="normal 400 16px Lato, sans-serif"/>
  <Variable name="sharing.text.color" description="Sharing text color" type="color" default="#000"  value="rgba(255, 255, 255, 0.87)"/>
  <Variable name="sharing.icon.color" description="Sharing icons color" type="color" default="#bf8b38"  value="#77e4ff"/>
</Group>

<Group description="Attribution">
  <Variable name="attribution.text.font" description="Attribution text font" type="font" default="$(montserrat12)"  value="normal 700 12px Lato, sans-serif"/>
  <Variable name="attribution.text.color" description="Attribution text color" type="color" default="rgba(0, 0, 0, 0.54)"  value="rgba(255, 255, 255, 0.54)"/>
  <Variable name="attribution.icon.color" description="Attribution icon color" type="color" default="rgba(0, 0, 0, 0.54)" hideEditor="true"  value="rgba(255, 255, 255, 0.54)"/>
</Group>

<Group description="Widths" selector="#main, html[dir=rtl] .sidebar-container, html[dir=ltr] .sidebar-container">
  <Variable name="sidebar.width" description="Sidebar width" type="length"
            min="100px" max="1000px" default="284px"  value="284px"/>
  <Variable name="content.width" description="Content width" type="length"
            min="660px" max="2400px" default="922px"  value="922px"/>
  <Variable name="content.margin" description="Content margin" type="length"
            min="0px" max="1000px" default="117px"  value="117px"/>
</Group>
 */

/*!************************************************
 * Blogger Template Style
 * Name: Soho
 **************************************************/
body{
overflow-wrap:break-word;
word-break:break-word;
word-wrap:break-word
}
.hidden{
display:none
}
.invisible{
visibility:hidden
}
.container::after,.float-container::after{
clear:both;
content:'';
display:table
}
.clearboth{
clear:both
}
#comments .comment .comment-actions,.subscribe-popup .FollowByEmail .follow-by-email-submit{
background:0 0;
border:0;
box-shadow:none;
color:$(body.link.color);
cursor:pointer;
font-size:14px;
font-weight:700;
outline:0;
text-decoration:none;
text-transform:uppercase;
width:auto
}
.dim-overlay{
background-color:rgba(0,0,0,.54);
height:100vh;
left:0;
position:fixed;
top:0;
width:100%
}
#sharing-dim-overlay{
background-color:transparent
}
input::-ms-clear{
display:none
}
.blogger-logo,.svg-icon-24.blogger-logo{
fill:#ff9800;
opacity:1
}
.loading-spinner-large{
-webkit-animation:mspin-rotate 1.568s infinite linear;
animation:mspin-rotate 1.568s infinite linear;
height:48px;
overflow:hidden;
position:absolute;
width:48px;
z-index:200
}
.loading-spinner-large>div{
-webkit-animation:mspin-revrot 5332ms infinite steps(4);
animation:mspin-revrot 5332ms infinite steps(4)
}
.loading-spinner-large>div>div{
-webkit-animation:mspin-singlecolor-large-film 1333ms infinite steps(81);
animation:mspin-singlecolor-large-film 1333ms infinite steps(81);
background-size:100%;
height:48px;
width:3888px
}
.mspin-black-large>div>div,.mspin-grey_54-large>div>div{
background-image:url(https://www.blogblog.com/indie/mspin_black_large.svg)
}
.mspin-white-large>div>div{
background-image:url(https://www.blogblog.com/indie/mspin_white_large.svg)
}
.mspin-grey_54-large{
opacity:.54
}
@-webkit-keyframes mspin-singlecolor-large-film{
from{
-webkit-transform:translateX(0);
transform:translateX(0)
}
to{
-webkit-transform:translateX(-3888px);
transform:translateX(-3888px)
}
}
@keyframes mspin-singlecolor-large-film{
from{
-webkit-transform:translateX(0);
transform:translateX(0)
}
to{
-webkit-transform:translateX(-3888px);
transform:translateX(-3888px)
}
}
@-webkit-keyframes mspin-rotate{
from{
-webkit-transform:rotate(0);
transform:rotate(0)
}
to{
-webkit-transform:rotate(360deg);
transform:rotate(360deg)
}
}
@keyframes mspin-rotate{
from{
-webkit-transform:rotate(0);
transform:rotate(0)
}
to{
-webkit-transform:rotate(360deg);
transform:rotate(360deg)
}
}
@-webkit-keyframes mspin-revrot{
from{
-webkit-transform:rotate(0);
transform:rotate(0)
}
to{
-webkit-transform:rotate(-360deg);
transform:rotate(-360deg)
}
}
@keyframes mspin-revrot{
from{
-webkit-transform:rotate(0);
transform:rotate(0)
}
to{
-webkit-transform:rotate(-360deg);
transform:rotate(-360deg)
}
}
.skip-navigation{
background-color:#fff;
box-sizing:border-box;
color:#000;
display:block;
height:0;
left:0;
line-height:50px;
overflow:hidden;
padding-top:0;
position:fixed;
text-align:center;
top:0;
-webkit-transition:box-shadow .3s,height .3s,padding-top .3s;
transition:box-shadow .3s,height .3s,padding-top .3s;
width:100%;
z-index:900
}
.skip-navigation:focus{
box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2);
height:50px
}
#main{
outline:0
}
.main-heading{
position:absolute;
clip:rect(1px,1px,1px,1px);
padding:0;
border:0;
height:1px;
width:1px;
overflow:hidden
}
.Attribution{
margin-top:1em;
text-align:center
}
.Attribution .blogger img,.Attribution .blogger svg{
vertical-align:bottom
}
.Attribution .blogger img{
margin-$endSide:.5em
}
.Attribution div{
line-height:24px;
margin-top:.5em
}
.Attribution .copyright,.Attribution .image-attribution{
font-size:.7em;
margin-top:1.5em
}
.BLOG_mobile_video_class{
display:none
}
.bg-photo{
background-attachment:scroll!important
}
body .CSS_LIGHTBOX{
z-index:900
}
.extendable .show-less,.extendable .show-more{
border-color:$(body.link.color);
color:$(body.link.color);
margin-top:8px
}
.extendable .show-less.hidden,.extendable .show-more.hidden{
display:none
}
.inline-ad{
display:none;
max-width:100%;
overflow:hidden
}
.adsbygoogle{
display:block
}
#cookieChoiceInfo{
bottom:0;
top:auto
}
iframe.b-hbp-video{
border:0
}
.post-body img{
max-width:100%
}
.post-body iframe{
max-width:100%
}
.post-body a[imageanchor="1"]{
display:inline-block
}
.byline{
margin-$endSide:1em
}
.byline:last-child{
margin-$endSide:0
}
.link-copied-dialog{
max-width:520px;
outline:0
}
.link-copied-dialog .modal-dialog-buttons{
margin-top:8px
}
.link-copied-dialog .goog-buttonset-default{
background:0 0;
border:0
}
.link-copied-dialog .goog-buttonset-default:focus{
outline:0
}
.paging-control-container{
margin-bottom:16px
}
.paging-control-container .paging-control{
display:inline-block
}
.paging-control-container .comment-range-text::after,.paging-control-container .paging-control{
color:$(body.link.color)
}
.paging-control-container .comment-range-text,.paging-control-container .paging-control{
margin-$endSide:8px
}
.paging-control-container .comment-range-text::after,.paging-control-container .paging-control::after{
content:'\00B7';
cursor:default;
padding-$startSide:8px;
pointer-events:none
}
.paging-control-container .comment-range-text:last-child::after,.paging-control-container .paging-control:last-child::after{
content:none
}
.byline.reactions iframe{
height:20px
}
.b-notification{
color:#000;
background-color:#fff;
border-bottom:solid 1px #000;
box-sizing:border-box;
padding:16px 32px;
text-align:center
}
.b-notification.visible{
-webkit-transition:margin-top .3s cubic-bezier(.4,0,.2,1);
transition:margin-top .3s cubic-bezier(.4,0,.2,1)
}
.b-notification.invisible{
position:absolute
}
.b-notification-close{
position:absolute;
right:8px;
top:8px
}
.no-posts-message{
line-height:40px;
text-align:center
}
@media screen and (max-width:$(content.width + 240px)){
body.item-view .post-body a[imageanchor="1"][style*="float: left;"],body.item-view .post-body a[imageanchor="1"][style*="float: right;"]{
float:none!important;
clear:none!important
}
body.item-view .post-body a[imageanchor="1"] img{
display:block;
height:auto;
margin:0 auto
}
body.item-view .post-body>.separator:first-child>a[imageanchor="1"]:first-child{
margin-top:20px
}
.post-body a[imageanchor]{
display:block
}
body.item-view .post-body a[imageanchor="1"]{
margin-left:0!important;
margin-right:0!important
}
body.item-view .post-body a[imageanchor="1"]+a[imageanchor="1"]{
margin-top:16px
}
}
.item-control{
display:none
}
#comments{
border-top:1px dashed rgba(0,0,0,.54);
margin-top:20px;
padding:20px
}
#comments .comment-thread ol{
margin:0;
padding-left:0;
padding-$startSide:0
}
#comments .comment .comment-replybox-single,#comments .comment-thread .comment-replies{
margin-left:60px
}
#comments .comment-thread .thread-count{
display:none
}
#comments .comment{
list-style-type:none;
padding:0 0 30px;
position:relative
}
#comments .comment .comment{
padding-bottom:8px
}
.comment .avatar-image-container{
position:absolute
}
.comment .avatar-image-container img{
border-radius:50%
}
.avatar-image-container svg,.comment .avatar-image-container .avatar-icon{
border-radius:50%;
border:solid 1px $(comment.author.color);
box-sizing:border-box;
fill:$(comment.author.color);
height:35px;
margin:0;
padding:7px;
width:35px
}
.comment .comment-block{
margin-top:10px;
margin-$startSide:60px;
padding-bottom:0
}
#comments .comment-author-header-wrapper{
margin-left:40px
}
#comments .comment .thread-expanded .comment-block{
padding-bottom:20px
}
#comments .comment .comment-header .user,#comments .comment .comment-header .user a{
color:$(comment.author.color);
font-style:normal;
font-weight:700
}
#comments .comment .comment-actions{
bottom:0;
margin-bottom:15px;
position:absolute
}
#comments .comment .comment-actions>*{
margin-right:8px
}
#comments .comment .comment-header .datetime{
bottom:0;
color:$(comment.header.color);
display:inline-block;
font-size:13px;
font-style:italic;
margin-$startSide:8px
}
#comments .comment .comment-footer .comment-timestamp a,#comments .comment .comment-header .datetime a{
color:$(comment.header.color)
}
#comments .comment .comment-content,.comment .comment-body{
margin-top:12px;
word-break:break-word
}
.comment-body{
margin-bottom:12px
}
#comments.embed[data-num-comments="0"]{
border:0;
margin-top:0;
padding-top:0
}
#comments.embed[data-num-comments="0"] #comment-post-message,#comments.embed[data-num-comments="0"] div.comment-form>p,#comments.embed[data-num-comments="0"] p.comment-footer{
display:none
}
#comment-editor-src{
display:none
}
.comments .comments-content .loadmore.loaded{
max-height:0;
opacity:0;
overflow:hidden
}
.extendable .remaining-items{
height:0;
overflow:hidden;
-webkit-transition:height .3s cubic-bezier(.4,0,.2,1);
transition:height .3s cubic-bezier(.4,0,.2,1)
}
.extendable .remaining-items.expanded{
height:auto
}
.svg-icon-24,.svg-icon-24-button{
cursor:pointer;
height:24px;
width:24px;
min-width:24px
}
.touch-icon{
margin:-12px;
padding:12px
}
.touch-icon:active,.touch-icon:focus{
background-color:rgba(153,153,153,.4);
border-radius:50%
}
svg:not(:root).touch-icon{
overflow:visible
}
html[dir=rtl] .rtl-reversible-icon{
-webkit-transform:scaleX(-1);
-ms-transform:scaleX(-1);
transform:scaleX(-1)
}
.svg-icon-24-button,.touch-icon-button{
background:0 0;
border:0;
margin:0;
outline:0;
padding:0
}
.touch-icon-button .touch-icon:active,.touch-icon-button .touch-icon:focus{
background-color:transparent
}
.touch-icon-button:active .touch-icon,.touch-icon-button:focus .touch-icon{
background-color:rgba(153,153,153,.4);
border-radius:50%
}
.Profile .default-avatar-wrapper .avatar-icon{
border-radius:50%;
border:solid 1px $(body.text.color);
box-sizing:border-box;
fill:$(body.text.color);
margin:0
}
.Profile .individual .default-avatar-wrapper .avatar-icon{
padding:25px
}
.Profile .individual .avatar-icon,.Profile .individual .profile-img{
height:120px;
width:120px
}
.Profile .team .default-avatar-wrapper .avatar-icon{
padding:8px
}
.Profile .team .avatar-icon,.Profile .team .default-avatar-wrapper,.Profile .team .profile-img{
height:40px;
width:40px
}
.snippet-container{
margin:0;
position:relative;
overflow:hidden
}
.snippet-fade{
bottom:0;
box-sizing:border-box;
position:absolute;
width:96px
}
.snippet-fade{
$endSide:0
}
.snippet-fade:after{
content:'\2026'
}
.snippet-fade:after{
float:$endSide
}
.centered-top-container.sticky{
left:0;
position:fixed;
right:0;
top:0;
width:auto;
z-index:50;
-webkit-transition-property:opacity,-webkit-transform;
transition-property:opacity,-webkit-transform;
transition-property:transform,opacity;
transition-property:transform,opacity,-webkit-transform;
-webkit-transition-duration:.2s;
transition-duration:.2s;
-webkit-transition-timing-function:cubic-bezier(.4,0,.2,1);
transition-timing-function:cubic-bezier(.4,0,.2,1)
}
.centered-top-placeholder{
display:none
}
.collapsed-header .centered-top-placeholder{
display:block
}
.centered-top-container .Header .replaced h1,.centered-top-placeholder .Header .replaced h1{
display:none
}
.centered-top-container.sticky .Header .replaced h1{
display:block
}
.centered-top-container.sticky .Header .header-widget{
background:0 0
}
.centered-top-container.sticky .Header .header-image-wrapper{
display:none
}
.centered-top-container img,.centered-top-placeholder img{
max-width:100%
}
.collapsible{
-webkit-transition:height .3s cubic-bezier(.4,0,.2,1);
transition:height .3s cubic-bezier(.4,0,.2,1)
}
.collapsible,.collapsible>summary{
display:block;
overflow:hidden
}
.collapsible>:not(summary){
display:none
}
.collapsible[open]>:not(summary){
display:block
}
.collapsible:focus,.collapsible>summary:focus{
outline:0
}
.collapsible>summary{
cursor:pointer;
display:block;
padding:0
}
.collapsible:focus>summary,.collapsible>summary:focus{
background-color:transparent
}
.collapsible>summary::-webkit-details-marker{
display:none
}
.collapsible-title{
-webkit-box-align:center;
-webkit-align-items:center;
-ms-flex-align:center;
align-items:center;
display:-webkit-box;
display:-webkit-flex;
display:-ms-flexbox;
display:flex
}
.collapsible-title .title{
-webkit-box-flex:1;
-webkit-flex:1 1 auto;
-ms-flex:1 1 auto;
flex:1 1 auto;
-webkit-box-ordinal-group:1;
-webkit-order:0;
-ms-flex-order:0;
order:0;
overflow:hidden;
text-overflow:ellipsis;
white-space:nowrap
}
.collapsible-title .chevron-down,.collapsible[open] .collapsible-title .chevron-up{
display:block
}
.collapsible-title .chevron-up,.collapsible[open] .collapsible-title .chevron-down{
display:none
}
.flat-button{
cursor:pointer;
display:inline-block;
font-weight:700;
text-transform:uppercase;
border-radius:2px;
padding:8px;
margin:-8px
}
.flat-icon-button{
background:0 0;
border:0;
margin:0;
outline:0;
padding:0;
margin:-12px;
padding:12px;
cursor:pointer;
box-sizing:content-box;
display:inline-block;
line-height:0
}
.flat-icon-button,.flat-icon-button .splash-wrapper{
border-radius:50%
}
.flat-icon-button .splash.animate{
-webkit-animation-duration:.3s;
animation-duration:.3s
}
.overflowable-container{
max-height:$(header.pageList.font.size * 2);
overflow:hidden;
position:relative
}
.overflow-button{
cursor:pointer
}
#overflowable-dim-overlay{
background:0 0
}
.overflow-popup{
box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12);
background-color:$(header.background.color);
left:0;
max-width:calc(100% - 32px);
position:absolute;
top:0;
visibility:hidden;
z-index:101
}
.overflow-popup ul{
list-style:none
}
.overflow-popup .tabs li,.overflow-popup li{
display:block;
height:auto
}
.overflow-popup .tabs li{
padding-left:0;
padding-right:0
}
.overflow-button.hidden,.overflow-popup .tabs li.hidden,.overflow-popup li.hidden{
display:none
}
.search{
display:-webkit-box;
display:-webkit-flex;
display:-ms-flexbox;
display:flex;
line-height:24px;
width:24px
}
.search.focused{
width:100%
}
.search.focused .section{
width:100%
}
.search form{
z-index:101
}
.search h3{
display:none
}
.search form{
display:-webkit-box;
display:-webkit-flex;
display:-ms-flexbox;
display:flex;
-webkit-box-flex:1;
-webkit-flex:1 0 0;
-ms-flex:1 0 0px;
flex:1 0 0;
border-bottom:solid 1px transparent;
padding-bottom:8px
}
.search form>*{
display:none
}
.search.focused form>*{
display:block
}
.search .search-input label{
display:none
}
.centered-top-placeholder.cloned .search form{
z-index:30
}
.search.focused form{
border-color:$(header.text.color);
position:relative;
width:auto
}
.collapsed-header .centered-top-container .search.focused form{
border-bottom-color:transparent
}
.search-expand{
-webkit-box-flex:0;
-webkit-flex:0 0 auto;
-ms-flex:0 0 auto;
flex:0 0 auto
}
.search-expand-text{
display:none
}
.search-close{
display:inline;
vertical-align:middle
}
.search-input{
-webkit-box-flex:1;
-webkit-flex:1 0 1px;
-ms-flex:1 0 1px;
flex:1 0 1px
}
.search-input input{
background:0 0;
border:0;
box-sizing:border-box;
color:$(header.text.color);
display:inline-block;
outline:0;
width:calc(100% - 48px)
}
.search-input input.no-cursor{
color:transparent;
text-shadow:0 0 0 $(header.text.color)
}
.collapsed-header .centered-top-container .search-action,.collapsed-header .centered-top-container .search-input input{
color:$(header.text.color)
}
.collapsed-header .centered-top-container .search-input input.no-cursor{
color:transparent;
text-shadow:0 0 0 $(header.text.color)
}
.collapsed-header .centered-top-container .search-input input.no-cursor:focus,.search-input input.no-cursor:focus{
outline:0
}
.search-focused>*{
visibility:hidden
}
.search-focused .search,.search-focused .search-icon{
visibility:visible
}
.search.focused .search-action{
display:block
}
.search.focused .search-action:disabled{
opacity:.3
}
.widget.Sharing .sharing-button{
display:none
}
.widget.Sharing .sharing-buttons li{
padding:0
}
.widget.Sharing .sharing-buttons li span{
display:none
}
.post-share-buttons{
position:relative
}
.centered-bottom .share-buttons .svg-icon-24,.share-buttons .svg-icon-24{
fill:$(body.text.color)
}
.sharing-open.touch-icon-button:active .touch-icon,.sharing-open.touch-icon-button:focus .touch-icon{
background-color:transparent
}
.share-buttons{
background-color:$(body.background.color);
border-radius:2px;
box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12);
color:$(body.text.color);
list-style:none;
margin:0;
padding:8px 0;
position:absolute;
top:-11px;
min-width:200px;
z-index:101
}
.share-buttons.hidden{
display:none
}
.sharing-button{
background:0 0;
border:0;
margin:0;
outline:0;
padding:0;
cursor:pointer
}
.share-buttons li{
margin:0;
height:48px
}
.share-buttons li:last-child{
margin-bottom:0
}
.share-buttons li .sharing-platform-button{
box-sizing:border-box;
cursor:pointer;
display:block;
height:100%;
margin-bottom:0;
padding:0 16px;
position:relative;
width:100%
}
.share-buttons li .sharing-platform-button:focus,.share-buttons li .sharing-platform-button:hover{
background-color:rgba(128,128,128,.1);
outline:0
}
.share-buttons li svg[class*=" sharing-"],.share-buttons li svg[class^=sharing-]{
position:absolute;
top:10px
}
.share-buttons li span.sharing-platform-button{
position:relative;
top:0
}
.share-buttons li .platform-sharing-text{
display:block;
font-size:16px;
line-height:48px;
white-space:nowrap
}
.share-buttons li .platform-sharing-text{
margin-$startSide:56px
}
.sidebar-container{
background-color:#f7f7f7;
max-width:$(sidebar.width);
overflow-y:auto;
-webkit-transition-property:-webkit-transform;
transition-property:-webkit-transform;
transition-property:transform;
transition-property:transform,-webkit-transform;
-webkit-transition-duration:.3s;
transition-duration:.3s;
-webkit-transition-timing-function:cubic-bezier(0,0,.2,1);
transition-timing-function:cubic-bezier(0,0,.2,1);
width:$(sidebar.width);
z-index:101;
-webkit-overflow-scrolling:touch
}
.sidebar-container .navigation{
line-height:0;
padding:16px
}
.sidebar-container .sidebar-back{
cursor:pointer
}
.sidebar-container .widget{
background:0 0;
margin:0 16px;
padding:16px 0
}
.sidebar-container .widget .title{
color:$(sidebar.widget.title.color);
margin:0
}
.sidebar-container .widget ul{
list-style:none;
margin:0;
padding:0
}
.sidebar-container .widget ul ul{
margin-$startSide:1em
}
.sidebar-container .widget li{
font-size:16px;
line-height:normal
}
.sidebar-container .widget+.widget{
border-top:1px dashed $(sidebar.separator.color)
}
.BlogArchive li{
margin:16px 0
}
.BlogArchive li:last-child{
margin-bottom:0
}
.Label li a{
display:inline-block
}
.BlogArchive .post-count,.Label .label-count{
float:$endSide;
margin-$startSide:.25em
}
.BlogArchive .post-count::before,.Label .label-count::before{
content:'('
}
.BlogArchive .post-count::after,.Label .label-count::after{
content:')'
}
.widget.Translate .skiptranslate>div{
display:block!important
}
.widget.Profile .profile-link{
display:-webkit-box;
display:-webkit-flex;
display:-ms-flexbox;
display:flex
}
.widget.Profile .team-member .default-avatar-wrapper,.widget.Profile .team-member .profile-img{
-webkit-box-flex:0;
-webkit-flex:0 0 auto;
-ms-flex:0 0 auto;
flex:0 0 auto;
margin-$endSide:1em
}
.widget.Profile .individual .profile-link{
-webkit-box-orient:vertical;
-webkit-box-direction:normal;
-webkit-flex-direction:column;
-ms-flex-direction:column;
flex-direction:column
}
.widget.Profile .team .profile-link .profile-name{
-webkit-align-self:center;
-ms-flex-item-align:center;
-ms-grid-row-align:center;
align-self:center;
display:block;
-webkit-box-flex:1;
-webkit-flex:1 1 auto;
-ms-flex:1 1 auto;
flex:1 1 auto
}
.dim-overlay{
background-color:rgba(0,0,0,.54);
z-index:100
}
body.sidebar-visible{
overflow-y:hidden
}
@media screen and (max-width:$(content.width + sidebar.width + content.margin * 2 - 1px)){
.sidebar-container{
bottom:0;
position:fixed;
top:0;
$startSide:0;
$endSide:auto
}
.sidebar-container.sidebar-invisible{
-webkit-transition-timing-function:cubic-bezier(.4,0,.6,1);
transition-timing-function:cubic-bezier(.4,0,.6,1)
}
html[dir=ltr] .sidebar-container.sidebar-invisible{
-webkit-transform:translateX($(sidebar.width * -1));
-ms-transform:translateX($(sidebar.width * -1));
transform:translateX($(sidebar.width * -1))
}
html[dir=rtl] .sidebar-container.sidebar-invisible{
-webkit-transform:translateX($(sidebar.width));
-ms-transform:translateX($(sidebar.width));
transform:translateX($(sidebar.width))
}
}
@media screen and (min-width:$(content.width + sidebar.width + content.margin * 2)){
.sidebar-container{
position:absolute;
top:0;
$startSide:0;
$endSide:auto
}
.sidebar-container .navigation{
display:none
}
}
.dialog{
box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12);
background:$(body.background.color);
box-sizing:border-box;
color:$(body.text.color);
padding:30px;
position:fixed;
text-align:center;
width:calc(100% - 24px);
z-index:101
}
.dialog input[type=email],.dialog input[type=text]{
background-color:transparent;
border:0;
border-bottom:solid 1px rgba($(body.text.color.red),$(body.text.color.green),$(body.text.color.blue),.12);
color:$(body.text.color);
display:block;
font-family:$(body.text.font.family);
font-size:16px;
line-height:24px;
margin:auto;
padding-bottom:7px;
outline:0;
text-align:center;
width:100%
}
.dialog input[type=email]::-webkit-input-placeholder,.dialog input[type=text]::-webkit-input-placeholder{
color:$(body.text.color)
}
.dialog input[type=email]::-moz-placeholder,.dialog input[type=text]::-moz-placeholder{
color:$(body.text.color)
}
.dialog input[type=email]:-ms-input-placeholder,.dialog input[type=text]:-ms-input-placeholder{
color:$(body.text.color)
}
.dialog input[type=email]::placeholder,.dialog input[type=text]::placeholder{
color:$(body.text.color)
}
.dialog input[type=email]:focus,.dialog input[type=text]:focus{
border-bottom:solid 2px $(body.link.color);
padding-bottom:6px
}
.dialog input.no-cursor{
color:transparent;
text-shadow:0 0 0 $(body.text.color)
}
.dialog input.no-cursor:focus{
outline:0
}
.dialog input.no-cursor:focus{
outline:0
}
.dialog input[type=submit]{
font-family:$(body.text.font.family)
}
.dialog .goog-buttonset-default{
color:$(body.link.color)
}
.subscribe-popup{
max-width:364px
}
.subscribe-popup h3{
color:$(body.title.color);
font-size:1.8em;
margin-top:0
}
.subscribe-popup .FollowByEmail h3{
display:none
}
.subscribe-popup .FollowByEmail .follow-by-email-submit{
color:$(body.link.color);
display:inline-block;
margin:0 auto;
margin-top:24px;
width:auto;
white-space:normal
}
.subscribe-popup .FollowByEmail .follow-by-email-submit:disabled{
cursor:default;
opacity:.3
}
@media (max-width:800px){
.blog-name div.widget.Subscribe{
margin-bottom:16px
}
body.item-view .blog-name div.widget.Subscribe{
margin:8px auto 16px auto;
width:100%
}
}
body#layout .bg-photo,body#layout .bg-photo-overlay{
display:none
}
body#layout .page_body{
padding:0;
position:relative;
top:0
}
body#layout .page{
display:inline-block;
left:inherit;
position:relative;
vertical-align:top;
width:540px
}
body#layout .centered{
max-width:954px
}
body#layout .navigation{
display:none
}
body#layout .sidebar-container{
display:inline-block;
width:40%
}
body#layout .hamburger-menu,body#layout .search{
display:none
}
body{
background-color:$(body.background.color);
color:$(body.text.color);
font:$(body.text.font);
height:100%;
margin:0;
min-height:100vh
}
h1,h2,h3,h4,h5,h6{
font-weight:400
}
a{
color:$(body.link.color);
text-decoration:none
}
.dim-overlay{
z-index:100
}
body.sidebar-visible .page_body{
overflow-y:scroll
}
.widget .title{
color:$(body.widget.title.color);
font:$(body.widget.title.font.small)
}
.extendable .show-less,.extendable .show-more{
color:$(body.action.color);
font:$(body.action.font.small);
margin:12px -8px 0 -8px;
text-transform:uppercase
}
.footer .widget,.main .widget{
margin:50px 0
}
.main .widget .title{
text-transform:uppercase
}
.inline-ad{
display:block;
margin-top:50px
}
.adsbygoogle{
text-align:center
}
.page_body{
display:-webkit-box;
display:-webkit-flex;
display:-ms-flexbox;
display:flex;
-webkit-box-orient:vertical;
-webkit-box-direction:normal;
-webkit-flex-direction:column;
-ms-flex-direction:column;
flex-direction:column;
min-height:100vh;
position:relative;
z-index:20
}
.page_body>*{
-webkit-box-flex:0;
-webkit-flex:0 0 auto;
-ms-flex:0 0 auto;
flex:0 0 auto
}
.page_body>#footer{
margin-top:auto
}
.centered-bottom,.centered-top{
margin:0 32px;
max-width:100%
}
.centered-top{
padding-bottom:12px;
padding-top:12px
}
.sticky .centered-top{
padding-bottom:0;
padding-top:0
}
.centered-top-container,.centered-top-placeholder{
background:$(header.background.color)
}
.centered-top{
display:-webkit-box;
display:-webkit-flex;
display:-ms-flexbox;
display:flex;
-webkit-flex-wrap:wrap;
-ms-flex-wrap:wrap;
flex-wrap:wrap;
-webkit-box-pack:justify;
-webkit-justify-content:space-between;
-ms-flex-pack:justify;
justify-content:space-between;
position:relative
}
.sticky .centered-top{
-webkit-flex-wrap:nowrap;
-ms-flex-wrap:nowrap;
flex-wrap:nowrap
}
.centered-top-container .svg-icon-24,.centered-top-placeholder .svg-icon-24{
fill:$(header.icon.color)
}
.back-button-container,.hamburger-menu-container{
-webkit-box-flex:0;
-webkit-flex:0 0 auto;
-ms-flex:0 0 auto;
flex:0 0 auto;
height:48px;
-webkit-box-ordinal-group:2;
-webkit-order:1;
-ms-flex-order:1;
order:1
}
.sticky .back-button-container,.sticky .hamburger-menu-container{
-webkit-box-ordinal-group:2;
-webkit-order:1;
-ms-flex-order:1;
order:1
}
.back-button,.hamburger-menu,.search-expand-icon{
cursor:pointer;
margin-top:0
}
.search{
-webkit-box-align:start;
-webkit-align-items:flex-start;
-ms-flex-align:start;
align-items:flex-start;
-webkit-box-flex:0;
-webkit-flex:0 0 auto;
-ms-flex:0 0 auto;
flex:0 0 auto;
height:48px;
margin-$startSide:24px;
-webkit-box-ordinal-group:4;
-webkit-order:3;
-ms-flex-order:3;
order:3
}
.search,.search.focused{
width:auto
}
.search.focused{
position:static
}
.sticky .search{
display:none;
-webkit-box-ordinal-group:5;
-webkit-order:4;
-ms-flex-order:4;
order:4
}
.search .section{
$endSide:0;
margin-top:12px;
position:absolute;
top:12px;
width:0
}
.sticky .search .section{
top:0
}
.search-expand{
background:0 0;
border:0;
margin:0;
outline:0;
padding:0;
color:$(body.action.color);
cursor:pointer;
-webkit-box-flex:0;
-webkit-flex:0 0 auto;
-ms-flex:0 0 auto;
flex:0 0 auto;
font:$(body.action.font.small);
text-transform:uppercase;
word-break:normal
}
.search.focused .search-expand{
visibility:hidden
}
.search .dim-overlay{
background:0 0
}
.search.focused .section{
max-width:400px
}
.search.focused form{
border-color:$(header.icon.color);
height:24px
}
.search.focused .search-input{
display:-webkit-box;
display:-webkit-flex;
display:-ms-flexbox;
display:flex;
-webkit-box-flex:1;
-webkit-flex:1 1 auto;
-ms-flex:1 1 auto;
flex:1 1 auto
}
.search-input input{
-webkit-box-flex:1;
-webkit-flex:1 1 auto;
-ms-flex:1 1 auto;
flex:1 1 auto;
font:$(search.input.font)
}
.search input[type=submit]{
display:none
}
.subscribe-section-container{
-webkit-box-flex:1;
-webkit-flex:1 0 auto;
-ms-flex:1 0 auto;
flex:1 0 auto;
margin-$startSide:24px;
-webkit-box-ordinal-group:3;
-webkit-order:2;
-ms-flex-order:2;
order:2;
text-align:$endSide
}
.sticky .subscribe-section-container{
-webkit-box-flex:0;
-webkit-flex:0 0 auto;
-ms-flex:0 0 auto;
flex:0 0 auto;
-webkit-box-ordinal-group:4;
-webkit-order:3;
-ms-flex-order:3;
order:3
}
.subscribe-button{
background:0 0;
border:0;
margin:0;
outline:0;
padding:0;
color:$(body.action.color);
cursor:pointer;
display:inline-block;
font:$(body.action.font.small);
line-height:48px;
margin:0;
text-transform:uppercase;
word-break:normal
}
.subscribe-popup h3{
color:$(body.widget.title.color);
font:$(body.widget.title.font.small);
margin-bottom:24px;
text-transform:uppercase
}
.subscribe-popup div.widget.FollowByEmail .follow-by-email-address{
color:$(body.text.color);
font:$(body.widget.title.font.small)
}
.subscribe-popup div.widget.FollowByEmail .follow-by-email-submit{
color:$(body.action.color);
font:$(body.action.font.small);
margin-top:24px;
text-transform:uppercase
}
.blog-name{
-webkit-box-flex:1;
-webkit-flex:1 1 100%;
-ms-flex:1 1 100%;
flex:1 1 100%;
-webkit-box-ordinal-group:5;
-webkit-order:4;
-ms-flex-order:4;
order:4;
overflow:hidden
}
.sticky .blog-name{
-webkit-box-flex:1;
-webkit-flex:1 1 auto;
-ms-flex:1 1 auto;
flex:1 1 auto;
margin:0 12px;
-webkit-box-ordinal-group:3;
-webkit-order:2;
-ms-flex-order:2;
order:2
}
body.search-view .centered-top.search-focused .blog-name{
display:none
}
.widget.Header h1{
font:$(header.title.font.small);
margin:0;
text-transform:uppercase
}
.widget.Header h1,.widget.Header h1 a{
color:$(header.title.color)
}
.widget.Header p{
color:$(header.text.color);
font:$(header.text.font);
line-height:1.7
}
.sticky .widget.Header h1{
font-size:16px;
line-height:48px;
overflow:hidden;
overflow-wrap:normal;
text-overflow:ellipsis;
white-space:nowrap;
word-wrap:normal
}
.sticky .widget.Header p{
display:none
}
.sticky{
box-shadow:0 1px 3px $(shadowColor)
}
#page_list_top .widget.PageList{
font:$(header.pageList.font);
line-height:$(header.pageList.font.size * 2)
}
#page_list_top .widget.PageList .title{
display:none
}
#page_list_top .widget.PageList .overflowable-contents{
overflow:hidden
}
#page_list_top .widget.PageList .overflowable-contents ul{
list-style:none;
margin:0;
padding:0
}
#page_list_top .widget.PageList .overflow-popup ul{
list-style:none;
margin:0;
padding:0 20px
}
#page_list_top .widget.PageList .overflowable-contents li{
display:inline-block
}
#page_list_top .widget.PageList .overflowable-contents li.hidden{
display:none
}
#page_list_top .widget.PageList .overflowable-contents li:not(:first-child):before{
color:$(header.pageList.color);
content:'\00b7'
}
#page_list_top .widget.PageList .overflow-button a,#page_list_top .widget.PageList .overflow-popup li a,#page_list_top .widget.PageList .overflowable-contents li a{
color:$(header.pageList.color);
font:$(header.pageList.font);
line-height:$(header.pageList.font.size * 2);
text-transform:uppercase
}
#page_list_top .widget.PageList .overflow-popup li.selected a,#page_list_top .widget.PageList .overflowable-contents li.selected a{
color:$(header.pageList.selected.color);
font:$(header.pageList.selected.font);
line-height:$(header.pageList.font.size * 2)
}
#page_list_top .widget.PageList .overflow-button{
display:inline
}
.sticky #page_list_top{
display:none
}
body.homepage-view .hero-image.has-image{
background:$(body.background);
background-attachment:scroll;
background-color:$(body.background.color);
background-size:cover;
height:62.5vw;
max-height:75vh;
min-height:200px;
width:100%
}
.post-filter-message{
background-color:$(body.filter.background.color);
color:$(body.filter.text.color);
display:-webkit-box;
display:-webkit-flex;
display:-ms-flexbox;
display:flex;
-webkit-flex-wrap:wrap;
-ms-flex-wrap:wrap;
flex-wrap:wrap;
font:$(body.filter.text.font.small);
-webkit-box-pack:justify;
-webkit-justify-content:space-between;
-ms-flex-pack:justify;
justify-content:space-between;
margin-top:50px;
padding:18px
}
.post-filter-message .message-container{
-webkit-box-flex:1;
-webkit-flex:1 1 auto;
-ms-flex:1 1 auto;
flex:1 1 auto;
min-width:0
}
.post-filter-message .home-link-container{
-webkit-box-flex:0;
-webkit-flex:0 0 auto;
-ms-flex:0 0 auto;
flex:0 0 auto
}
.post-filter-message .search-label,.post-filter-message .search-query{
color:$(body.filter.keyword.color);
font:$(body.filter.keyword.font.small);
text-transform:uppercase
}
.post-filter-message .home-link,.post-filter-message .home-link a{
color:$(body.filter.link.color);
font:$(body.filter.link.font.small);
text-transform:uppercase
}
.widget.FeaturedPost .thumb.hero-thumb{
background-position:center;
background-size:cover;
height:360px
}
.widget.FeaturedPost .featured-post-snippet:before{
content:'\2014'
}
.snippet-container,.snippet-fade{
font:$(post.text.font.small);
line-height:$(post.text.font.small.size * 1.7)
}
.snippet-container{
max-height:$(post.text.font.small.size * 1.7 * 7);
overflow:hidden
}
.snippet-fade{
background:-webkit-linear-gradient($startSide,$(body.background.color) 0,$(body.background.color) 20%,$(body.background.color.transparent) 100%);
background:linear-gradient(to $startSide,$(body.background.color) 0,$(body.background.color) 20%,$(body.background.color.transparent) 100%);
color:$(post.text.color)
}
.post-sidebar{
display:none
}
.widget.Blog .blog-posts .post-outer-container{
width:100%
}
.no-posts{
text-align:center
}
body.feed-view .widget.Blog .blog-posts .post-outer-container,body.item-view .widget.Blog .blog-posts .post-outer{
margin-bottom:50px
}
.widget.Blog .post.no-featured-image,.widget.PopularPosts .post.no-featured-image{
background-color:$(post.text.background.color);
padding:30px
}
.widget.Blog .post>.post-share-buttons-top{
$endSide:0;
position:absolute;
top:0
}
.widget.Blog .post>.post-share-buttons-bottom{
bottom:0;
$endSide:0;
position:absolute
}
.blog-pager{
text-align:$endSide
}
.blog-pager a{
color:$(body.action.color);
font:$(body.action.font.small);
text-transform:uppercase
}
.blog-pager .blog-pager-newer-link,.blog-pager .home-link{
display:none
}
.post-title{
font:$(post.title.font.small);
margin:0;
text-transform:uppercase
}
.post-title,.post-title a{
color:$(post.title.color)
}
.post.no-featured-image .post-title,.post.no-featured-image .post-title a{
color:$(post.text.title.color)
}
body.item-view .post-body-container:before{
content:'\2014'
}
.post-body{
color:$(post.text.color);
font:$(post.text.font.small);
line-height:1.7
}
.post-body blockquote{
color:$(post.blockquote.color);
font:$(post.blockquote.font.small);
line-height:1.7;
margin-left:0;
margin-right:0
}
.post-body img{
height:auto;
max-width:100%
}
.post-body .tr-caption{
color:$(post.caption.color);
font:$(post.caption.font);
line-height:1.7
}
.snippet-thumbnail{
position:relative
}
.snippet-thumbnail .post-header{
background:$(body.background.color);
bottom:0;
margin-bottom:0;
padding-$endSide:15px;
padding-bottom:5px;
padding-top:5px;
position:absolute
}
.snippet-thumbnail img{
width:100%
}
.post-footer,.post-header{
margin:8px 0
}
body.item-view .widget.Blog .post-header{
margin:0 0 16px 0
}
body.item-view .widget.Blog .post-footer{
margin:50px 0 0 0
}
.widget.FeaturedPost .post-footer{
display:-webkit-box;
display:-webkit-flex;
display:-ms-flexbox;
display:flex;
-webkit-flex-wrap:wrap;
-ms-flex-wrap:wrap;
flex-wrap:wrap;
-webkit-box-pack:justify;
-webkit-justify-content:space-between;
-ms-flex-pack:justify;
justify-content:space-between
}
.widget.FeaturedPost .post-footer>*{
-webkit-box-flex:0;
-webkit-flex:0 1 auto;
-ms-flex:0 1 auto;
flex:0 1 auto
}
.widget.FeaturedPost .post-footer,.widget.FeaturedPost .post-footer a,.widget.FeaturedPost .post-footer button{
line-height:1.7
}
.jump-link{
margin:-8px
}
.post-header,.post-header a,.post-header button{
color:$(post.header.color);
font:$(post.header.font)
}
.post.no-featured-image .post-header,.post.no-featured-image .post-header a,.post.no-featured-image .post-header button{
color:$(post.text.header.color)
}
.post-footer,.post-footer a,.post-footer button{
color:$(post.footer.color);
font:$(post.footer.font)
}
.post.no-featured-image .post-footer,.post.no-featured-image .post-footer a,.post.no-featured-image .post-footer button{
color:$(post.text.footer.color)
}
body.item-view .post-footer-line{
line-height:2.3
}
.byline{
display:inline-block
}
.byline .flat-button{
text-transform:none
}
.post-header .byline:not(:last-child):after{
content:'\00b7'
}
.post-header .byline:not(:last-child){
margin-$endSide:0
}
.byline.post-labels a{
display:inline-block;
word-break:break-all
}
.byline.post-labels a:not(:last-child):after{
content:','
}
.byline.reactions .reactions-label{
line-height:22px;
vertical-align:top
}
.post-share-buttons{
margin-$startSide:0
}
.share-buttons{
background-color:$(sharing.background.color);
border-radius:0;
box-shadow:0 1px 1px 1px $(shadowColor);
color:$(sharing.text.color);
font:$(sharing.text.font)
}
.share-buttons .svg-icon-24{
fill:$(sharing.icon.color)
}
#comment-holder .continue{
display:none
}
#comment-editor{
margin-bottom:20px;
margin-top:20px
}
.widget.Attribution,.widget.Attribution .copyright,.widget.Attribution .copyright a,.widget.Attribution .image-attribution,.widget.Attribution .image-attribution a,.widget.Attribution a{
color:$(attribution.text.color);
font:$(attribution.text.font)
}
.widget.Attribution svg{
fill:$(attribution.icon.color)
}
.widget.Attribution .blogger a{
display:-webkit-box;
display:-webkit-flex;
display:-ms-flexbox;
display:flex;
-webkit-align-content:center;
-ms-flex-line-pack:center;
align-content:center;
-webkit-box-pack:center;
-webkit-justify-content:center;
-ms-flex-pack:center;
justify-content:center;
line-height:24px
}
.widget.Attribution .blogger svg{
margin-$endSide:8px
}
.widget.Profile ul{
list-style:none;
padding:0
}
.widget.Profile .individual .default-avatar-wrapper,.widget.Profile .individual .profile-img{
border-radius:50%;
display:inline-block;
height:120px;
width:120px
}
.widget.Profile .individual .profile-data a,.widget.Profile .team .profile-name{
color:$(body.title.color);
font:$(body.title.font.small);
text-transform:none
}
.widget.Profile .individual dd{
color:$(body.text.color);
font:$(body.text.font);
margin:0 auto
}
.widget.Profile .individual .profile-link,.widget.Profile .team .visit-profile{
color:$(body.action.color);
font:$(body.action.font.small);
text-transform:uppercase
}
.widget.Profile .team .default-avatar-wrapper,.widget.Profile .team .profile-img{
border-radius:50%;
float:$startSide;
height:40px;
width:40px
}
.widget.Profile .team .profile-link .profile-name-wrapper{
-webkit-box-flex:1;
-webkit-flex:1 1 auto;
-ms-flex:1 1 auto;
flex:1 1 auto
}
.widget.Label li,.widget.Label span.label-size{
color:$(body.action.color);
display:inline-block;
font:$(body.action.font.small);
word-break:break-all
}
.widget.Label li:not(:last-child):after,.widget.Label span.label-size:not(:last-child):after{
content:','
}
.widget.PopularPosts .post{
margin-bottom:50px
}
#comments{
border-top:none;
padding:0
}
#comments .comment .comment-footer,#comments .comment .comment-header,#comments .comment .comment-header .datetime,#comments .comment .comment-header .datetime a{
color:$(comment.header.color);
font:$(comment.header.font)
}
#comments .comment .comment-author,#comments .comment .comment-author a,#comments .comment .comment-header .user,#comments .comment .comment-header .user a{
color:$(comment.author.color);
font:$(comment.author.font)
}
#comments .comment .comment-body,#comments .comment .comment-content{
color:$(comment.content.color);
font:$(comment.content.font)
}
#comments .comment .comment-actions,#comments .footer,#comments .footer a,#comments .loadmore,#comments .paging-control{
color:$(comment.action.color);
font:$(comment.action.font);
text-transform:uppercase
}
#commentsHolder{
border-bottom:none;
border-top:none
}
#comments .comment-form h4{
position:absolute;
clip:rect(1px,1px,1px,1px);
padding:0;
border:0;
height:1px;
width:1px;
overflow:hidden
}
.sidebar-container{
background-color:$(sidebar.background.color);
color:$(sidebar.widget.text.color);
font:$(sidebar.widget.text.font);
min-height:100%
}
html[dir=ltr] .sidebar-container{
box-shadow:1px 0 3px $(shadowColor)
}
html[dir=rtl] .sidebar-container{
box-shadow:-1px 0 3px $(shadowColor)
}
.sidebar-container a{
color:$(sidebar.action.color)
}
.sidebar-container .svg-icon-24{
fill:$(sidebar.icon.color)
}
.sidebar-container .widget{
margin:0;
margin-$startSide:40px;
padding:40px;
padding-$startSide:0
}
.sidebar-container .widget+.widget{
border-top:1px solid $(sidebar.separator.color)
}
.sidebar-container .widget .title{
color:$(sidebar.widget.title.color);
font:$(sidebar.widget.title.font)
}
.sidebar-container .widget ul li,.sidebar-container .widget.BlogArchive #ArchiveList li{
font:$(sidebar.widget.text.font);
margin:1em 0 0 0
}
.sidebar-container .BlogArchive .post-count,.sidebar-container .Label .label-count{
float:none
}
.sidebar-container .Label li a{
display:inline
}
.sidebar-container .widget.Profile .default-avatar-wrapper .avatar-icon{
border-color:$(sidebar.profile.name.color);
fill:$(sidebar.profile.name.color)
}
.sidebar-container .widget.Profile .individual{
text-align:center
}
.sidebar-container .widget.Profile .individual dd:before{
content:'\2014';
display:block
}
.sidebar-container .widget.Profile .individual .profile-data a,.sidebar-container .widget.Profile .team .profile-name{
color:$(sidebar.profile.name.color);
font:$(sidebar.profile.name.font)
}
.sidebar-container .widget.Profile .individual dd{
color:$(sidebar.profile.description.color);
font:$(sidebar.profile.description.font);
margin:0 30px
}
.sidebar-container .widget.Profile .individual .profile-link,.sidebar-container .widget.Profile .team .visit-profile{
color:$(sidebar.action.color);
font:$(sidebar.action.font)
}
.sidebar-container .snippet-fade{
background:-webkit-linear-gradient($startSide,$(sidebar.background.color) 0,$(sidebar.background.color) 20%,$(sidebar.background.color.transparent) 100%);
background:linear-gradient(to $startSide,$(sidebar.background.color) 0,$(sidebar.background.color) 20%,$(sidebar.background.color.transparent) 100%)
}
@media screen and (min-width:640px){
.centered-bottom,.centered-top{
margin:0 auto;
width:576px
}
.centered-top{
-webkit-flex-wrap:nowrap;
-ms-flex-wrap:nowrap;
flex-wrap:nowrap;
padding-bottom:24px;
padding-top:36px
}
.blog-name{
-webkit-box-flex:1;
-webkit-flex:1 1 auto;
-ms-flex:1 1 auto;
flex:1 1 auto;
min-width:0;
-webkit-box-ordinal-group:3;
-webkit-order:2;
-ms-flex-order:2;
order:2
}
.sticky .blog-name{
margin:0
}
.back-button-container,.hamburger-menu-container{
margin-$endSide:36px;
-webkit-box-ordinal-group:2;
-webkit-order:1;
-ms-flex-order:1;
order:1
}
.search{
margin-$startSide:36px;
-webkit-box-ordinal-group:5;
-webkit-order:4;
-ms-flex-order:4;
order:4
}
.search .section{
top:36px
}
.sticky .search{
display:block
}
.subscribe-section-container{
-webkit-box-flex:0;
-webkit-flex:0 0 auto;
-ms-flex:0 0 auto;
flex:0 0 auto;
margin-$startSide:36px;
-webkit-box-ordinal-group:4;
-webkit-order:3;
-ms-flex-order:3;
order:3
}
.subscribe-button{
font:$(body.action.font.large);
line-height:48px
}
.subscribe-popup h3{
font:$(body.widget.title.font.large)
}
.subscribe-popup div.widget.FollowByEmail .follow-by-email-address{
font:$(body.widget.title.font.large)
}
.subscribe-popup div.widget.FollowByEmail .follow-by-email-submit{
font:$(body.action.font.large)
}
.widget .title{
font:$(body.widget.title.font.large)
}
.widget.Blog .post.no-featured-image,.widget.PopularPosts .post.no-featured-image{
padding:65px
}
.post-title{
font:$(post.title.font.large)
}
.blog-pager a{
font:$(body.action.font.large)
}
.widget.Header h1{
font:$(header.title.font.large)
}
.sticky .widget.Header h1{
font-size:24px
}
}
@media screen and (min-width:$(content.width + 240px)){
.centered-bottom,.centered-top{
width:$(content.width)
}
.back-button-container,.hamburger-menu-container{
margin-$endSide:48px
}
.search{
margin-$startSide:48px
}
.search-expand{
font:$(body.action.font.large);
line-height:48px
}
.search-expand-text{
display:block
}
.search-expand-icon{
display:none
}
.subscribe-section-container{
margin-$startSide:48px
}
.post-filter-message{
font:$(body.filter.text.font.large)
}
.post-filter-message .search-label,.post-filter-message .search-query{
font:$(body.filter.keyword.font.large)
}
.post-filter-message .home-link{
font:$(body.filter.link.font.large)
}
.widget.Blog .blog-posts .post-outer-container{
width:$(content.width / 2 - 10px)
}
body.item-view .widget.Blog .blog-posts .post-outer-container{
width:100%
}
body.item-view .widget.Blog .blog-posts .post-outer{
display:-webkit-box;
display:-webkit-flex;
display:-ms-flexbox;
display:flex
}
#comments,body.item-view .post-outer-container .inline-ad,body.item-view .widget.PopularPosts{
margin-$startSide:220px;
width:$(content.width - 240px)
}
.post-sidebar{
box-sizing:border-box;
display:block;
font:$(body.action.font.large);
padding-$endSide:20px;
width:220px
}
.post-sidebar-item{
margin-bottom:30px
}
.post-sidebar-item ul{
list-style:none;
padding:0
}
.post-sidebar-item .sharing-button{
color:$(body.action.color);
cursor:pointer;
display:inline-block;
font:$(body.action.font.large);
line-height:normal;
word-break:normal
}
.post-sidebar-labels li{
margin-bottom:8px
}
body.item-view .widget.Blog .post{
width:$(content.width - 240px)
}
.widget.Blog .post.no-featured-image,.widget.PopularPosts .post.no-featured-image{
padding:100px 65px
}
.page .widget.FeaturedPost .post-content{
display:-webkit-box;
display:-webkit-flex;
display:-ms-flexbox;
display:flex;
-webkit-box-pack:justify;
-webkit-justify-content:space-between;
-ms-flex-pack:justify;
justify-content:space-between
}
.page .widget.FeaturedPost .thumb-link{
display:-webkit-box;
display:-webkit-flex;
display:-ms-flexbox;
display:flex
}
.page .widget.FeaturedPost .thumb.hero-thumb{
height:auto;
min-height:300px;
width:$(content.width / 2 - 10px)
}
.page .widget.FeaturedPost .post-content.has-featured-image .post-text-container{
width:425px
}
.page .widget.FeaturedPost .post-content.no-featured-image .post-text-container{
width:100%
}
.page .widget.FeaturedPost .post-header{
margin:0 0 8px 0
}
.page .widget.FeaturedPost .post-footer{
margin:8px 0 0 0
}
.post-body{
font:$(post.text.font.large);
line-height:1.7
}
.post-body blockquote{
font:$(post.blockquote.font.large);
line-height:1.7
}
.snippet-container,.snippet-fade{
font:$(post.text.font.large);
line-height:$(post.text.font.large.size * 1.7)
}
.snippet-container{
max-height:$(post.text.font.large.size * 1.7 * 12)
}
.widget.Profile .individual .profile-data a,.widget.Profile .team .profile-name{
font:$(body.title.font.large)
}
.widget.Profile .individual .profile-link,.widget.Profile .team .visit-profile{
font:$(body.action.font.large)
}
}
@media screen and (min-width:$(content.width + sidebar.width + content.margin * 2)){
body{
position:relative
}
.page_body{
margin-$startSide:$(sidebar.width)
}
.sticky .centered-top{
padding-$startSide:$(sidebar.width)
}
.hamburger-menu-container{
display:none
}
.sidebar-container{
overflow:visible;
z-index:32
}
}
]]></b:skin>
    <b:template-skin>
      <![CDATA[
      body#layout .hidden,
      body#layout .invisible {
        display: inherit;
      }
      body#layout .page {
        width: 60%;
      }
      body#layout.ltr .page {
        float: right;
      }
      body#layout.rtl .page {
        float: left;
      }
      body#layout .sidebar-container {
        width: 40%;
      }
      body#layout.ltr .sidebar-container {
        float: left;
      }
      body#layout.rtl .sidebar-container {
        float: right;
      }
      ]]>
    </b:template-skin>
    <b:defaultmarkups>
      <b:defaultmarkup type='Common'>
        <b:includable id='responsiveImage' var='settings'>
          <b:comment>Add in the high-res thumb for youtube images.</b:comment>
          <b:if cond='not data:settings.image.isYoutube'>
            <b:include data='settings' name='super.responsiveImage'/>
          <b:else/>
            <b:with value='resizeImage(data:post.featuredImage.youtubeMaxResDefaultUrl, 1152, &quot;4:3&quot;)' var='highRes'>
              <b:include data='{                                  image: data:settings.image,                                  imageSizes: [320,490],                                  sourceSizes: &quot;(max-width: 640px) 100vw, (max-width: 1024px) 576px, 490px&quot;,                                  enhancedSourceset: data:highRes                                }' name='super.responsiveImage'/>
            </b:with>
          </b:if>
        </b:includable>
      </b:defaultmarkup>
      <b:defaultmarkup type='BlogSearch'>
        <b:includable id='searchSubmit'>
          <b:if cond='data:widget.sectionId == &quot;search_top&quot;'>
            <label>
              <input type='submit'/>
              <b:include data='{ iconClass: &quot;touch-icon search-icon&quot; }' name='searchIcon'/>
            </label>
          <b:else/>
            <b:include name='super.searchSubmit'/>
          </b:if>
        </b:includable>
      </b:defaultmarkup>
      <b:defaultmarkup type='AdSense,Blog'>
        <b:includable id='defaultAdUnit'>
          <!-- Clear out style (need non-empty string) -->
          <b:with value='&quot;/* Done in css. */&quot;' var='style'>
            <b:include name='super.defaultAdUnit'/>
          </b:with>
        </b:includable>
      </b:defaultmarkup>
      <b:defaultmarkup type='Blog,FeaturedPost,PopularPosts'>
        <b:includable id='sharingButtonContent'>
          <b:message name='messages.share'/>
        </b:includable>
        <b:includable id='postLabels'>
          <b:include cond='data:view.isSingleItem and data:widget.type == &quot;Blog&quot;' name='super.postLabels'/>
        </b:includable>
        <b:includable id='headerByline'>
          <b:if cond='data:view.isSingleItem and data:widget.type == &quot;Blog&quot;'>
            <b:include name='super.headerByline'/>
          <b:else/>
            <b:include data='{ items: [&quot;author&quot;, &quot;timestamp&quot;] }' name='headerBylineOverride'/>
          </b:if>
        </b:includable>
        <b:includable id='footerBylines'>
          <b:if cond='data:view.isSingleItem and data:widget.type == &quot;Blog&quot;'>
            <b:include name='super.footerBylines'/>
          <b:else/>
            <b:include data='{ items: [[&quot;share&quot;, &quot;comments&quot;]] }' name='footerBylinesOverride'/>
          </b:if>
        </b:includable>
        <b:includable id='emailPostIcon'>
          <!-- Replace icon with text -->
          <span class='byline'>
            <a class='flat-button' expr:href='data:post.emailPostUrl'><data:messages.emailPost/></a>
          </span>
        </b:includable>
      </b:defaultmarkup>
      <b:defaultmarkup type='Blog'>
        <b:includable id='main'>
          <b:if cond='not data:posts.any'>
            <div class='no-posts'>
              <b:eval expr='data:view.isSearch ? data:messages.noResultsFound : data:messages.theresNothingHere'/>
            </div>
          </b:if>

          <!-- Display title on homepage -->
          <b:if cond='data:posts.any and data:view.isHomepage'>
            <h3 class='title'><data:messages.latestPosts/></h3>
          </b:if>
          <!-- Filter out the featured post, but only on the homepage. -->
          <b:with value='(data:widgets.FeaturedPost filter w =&gt; w.sectionId == &quot;page_body&quot;) map (w =&gt; w.postId)' var='featuredPostIds'>
            <b:with value='data:view.isHomepage ? data:posts filter (post =&gt; post.id not in data:featuredPostIds) : data:posts' var='posts'>
              <b:include name='super.main'/>
            </b:with>
          </b:with>
        </b:includable>
        <b:includable id='postCommentsAndAd' var='post'>
          <!-- Always render inline ad inside container -->
          <div class='post-outer-container'>
            <div class='post-outer'>
              <b:include data='post' name='post'/>
            </div>
            <b:include cond='data:view.isSingleItem' data='post' name='commentPicker'/>
            <b:include cond='data:post.includeAd and data:post.adNumber lt (data:view.isHomepage ? 2 : 3)' data='post' name='inlineAd'/>
          </div>
        </b:includable>
        <b:includable id='post' var='post'>
          <b:if cond='data:view.isSingleItem'>
            <div class='post-sidebar'>
              <b:if cond='data:widgets.Blog.first.allBylineItems.share and data:post.shareUrl'>
                <div class='post-sidebar-item post-share-buttons'>
                  <b:with value='data:widget.instanceId + &quot;-&quot; + (data:regionName ?: &quot;byline&quot;) + &quot;-&quot; + data:post.id' var='sharingId'>
                    <b:include data='{                                                              sharingId: data:sharingId,                                                              originalUrl: data:post.url,                                                              shareUrl: data:post.shareUrl,                                                              platforms: data:blog.sharing.platforms,                                                            }' name='sharingButtons'/>
                  </b:with>
                </div>
              </b:if>
              <b:if cond='data:widgets.Blog.first.allBylineItems.labels and data:post.labels'>
                <div class='post-sidebar-item post-sidebar-labels'>
                  <div><data:messages.labels/></div>
                  <ul>
                    <b:loop index='i' values='data:post.labels' var='label'>
                      <li><a expr:href='data:label.url' rel='tag'><data:label.name/></a></li>
                    </b:loop>
                  </ul>
                </div>
              </b:if>
            </div>
          </b:if>
          <div class='post'>
            <b:class cond='data:view.isMultipleItems and data:post.featuredImage' name='has-featured-image'/>
            <b:class cond='data:view.isMultipleItems and not data:post.featuredImage' name='no-featured-image'/>
            <b:include data='post' name='postMeta'/>
            <b:if cond='data:view.isSingleItem'>
              <b:include name='headerByline'/>
              <b:include data='post' name='postTitle'/>
              <div class='post-body-container'>
                <b:include data='post' name='postBody'/>
              </div>
            <b:else/>
              <b:if cond='data:post.featuredImage'>
                <div class='snippet-thumbnail'>
                  <a expr:href='data:post.url'>
                    <b:comment>Max width is 576, so max size @ 2x is 1152.</b:comment>
                    <b:include data='{                                        image: data:post.featuredImage,                                        imageSizes: [320,490,576,1152],                                        sourceSizes: &quot;(max-width: 576px) 100vw, (max-width: 1024px) 576px, 490px&quot;                                      }' name='responsiveImage'/>
                  </a>
                  <b:include name='headerByline'/>
                </div>
              <b:else/>
                <b:include name='headerByline'/>
              </b:if>
              <b:include data='post' name='postTitle'/>
            </b:if>
            <b:include data='post' name='postFooter'/>
          </div>
        </b:includable>
        <b:includable id='feedLinks'>
          <!-- Don't render -->
        </b:includable>
      </b:defaultmarkup>
      <b:defaultmarkup type='BlogArchive'>
        <b:includable id='main' var='this'>
          <details class='collapsible extendable'>
            <b:attr cond='data:view.isArchive' name='open' value='open'/>
            <b:with value='true' var='renderAsDetails'>
            <b:with value='data:messages.archive' var='defaultTitle'>
              <b:include name='super.main'/>
            </b:with>
            </b:with>
          </details>
        </b:includable>
        <b:includable id='flat'>
          <b:include data='{                               buttonClass: &quot;flat-button&quot;,                               items: data:this.data,                               itemSet: &quot;data&quot;,                               itemsMarkup: &quot;super.flat&quot;                             }' name='extendableItems'/>
        </b:includable>
        <b:includable id='hierarchy'>
          <b:include data='{                               buttonClass: &quot;flat-button&quot;,                               limit: 1,                               items: data:this.data,                               itemSet: &quot;data&quot;,                               itemsMarkup: &quot;super.hierarchy&quot;                             }' name='extendableItems'/>
        </b:includable>
      </b:defaultmarkup>
      <b:defaultmarkup type='FeaturedPost'>
        <b:includable id='main'>
          <b:with value='data:messages.featured' var='defaultTitle'>
            <b:include name='super.main'/>
          </b:with>
        </b:includable>
        <b:includable id='snippetedPostContent'>
          <b:with value='data:postDisplay.showFeaturedImage and data:post.featuredImage' var='hasImage'>
            <div class='post-content'>
              <b:class cond='data:hasImage' name='has-featured-image'/>
              <b:class cond='not data:hasImage' name='no-featured-image'/>

              <!-- Change the order and add a snippet container -->
              <b:include cond='data:hasImage' data='post' name='snippetedPostThumbnail'/>
              <div class='post-text-container'>
                <b:include name='headerByline'/>
                <b:include cond='data:this.postDisplay.showTitle' name='snippetedPostTitle'/>
                <b:with value='&quot;featured-post&quot;' var='snippetPrefix'>
                  <b:include cond='data:this.postDisplay.showSnippet' data='post' name='postSnippet'/>
                </b:with>
                <div class='post-footer'>
                  <b:include name='footerBylines'/>
                  <b:include data='post' name='postJumpLink'/>
                </div>
              </div>
            </div>
          </b:with>
        </b:includable>
        <b:includable id='snippetedPostByline' var='post'>
          <b:include name='headerByline'/>
        </b:includable>
        <b:includable id='snippetedPostThumbnail'>
          <b:include data='{image: data:featuredImage, maxSize: 954, selector: &quot;.hero-thumb&quot;}' name='responsiveImageStyle'/>
          <a class='thumb-link' expr:href='data:post.url'><div class='thumb hero-thumb'/></a>
        </b:includable>
      </b:defaultmarkup>
      <b:defaultmarkup type='Header'>
        <b:includable id='image'>
          <b:include name='super.image'/>
          <!-- If we are replacing the title, force it to render anyway, and it'll be hidden in CSS. -->
          <b:include cond='data:this.imagePlacement == &quot;REPLACE&quot;' name='title'/>
        </b:includable>
        <b:includable id='title'>
          <div>
            <b:class cond='data:this.imagePlacement == &quot;REPLACE&quot;' name='replaced'/>
            <b:include name='super.title'/>
          </div>
        </b:includable>
      </b:defaultmarkup>
      <b:defaultmarkup type='Label'>
        <b:includable id='main' var='this'>
          <details class='collapsible extendable'>
            <b:attr cond='data:view.isLabelSearch' name='open' value='open'/>
            <b:with value='true' var='renderAsDetails'>
            <b:with value='data:messages.labels' var='defaultTitle'>
              <b:include name='super.main'/>
            </b:with>
            </b:with>
          </details>
        </b:includable>
        <b:includable id='list'>
          <b:include data='{                               buttonClass: &quot;flat-button&quot;,                               items: data:this.labels,                               itemSet: &quot;labels&quot;,                               itemsMarkup: &quot;super.list&quot;                             }' name='extendableItems'/>
        </b:includable>
        <b:includable id='cloud'>
          <b:include data='{                               buttonClass: &quot;flat-button&quot;,                               items: data:this.labels,                               itemSet: &quot;labels&quot;,                               itemsMarkup: &quot;super.cloud&quot;                             }' name='extendableItems'/>
        </b:includable>
      </b:defaultmarkup>
      <b:defaultmarkup type='PageList'>
        <b:includable id='content'>
          <div class='widget-content'>
            <b:if cond='data:widget.sectionId == &quot;page_list_top&quot;'>
              <b:include name='overflowablePageList'/>
            <b:else/>
              <b:include name='pageList'/>
            </b:if>
          </div>
        </b:includable>
        <b:includable id='overflowButton'>
          <a><data:messages.moreEllipsis/></a>
        </b:includable>
      </b:defaultmarkup>
      <b:defaultmarkup type='PopularPosts'>
        <b:includable id='main'>
          <!-- Default the title to 'Popular posts'. -->
          <b:with value='data:messages.popularPosts' var='defaultTitle'>
            <b:include name='super.main'/>
          </b:with>
        </b:includable>
        <b:includable id='snippetedPostContent'>
          <div class='post'>
            <b:class cond='data:post.featuredImage' name='has-featured-image'/>
            <b:class cond='not data:post.featuredImage' name='no-featured-image'/>
            <b:if cond='data:post.featuredImage'>
              <div class='snippet-thumbnail'>
                <a expr:href='data:post.url'>
                  <b:include data='{                                      image: data:post.featuredImage,                                      imageSizes: [330,660,1320],                                      sourceSizes: &quot;(max-width: 660px) 100vw, 660px&quot;                                    }' name='responsiveImage'/>
                </a>
                <b:include name='headerByline'/>
              </div>
            <b:else/>
              <b:include name='headerByline'/>
            </b:if>
            <b:include cond='data:this.postDisplay.showTitle' name='snippetedPostTitle'/>
            <div class='post-footer'>
              <b:include name='footerBylines'/>
            </div>
          </div>
        </b:includable>
      </b:defaultmarkup>
      <b:defaultmarkup type='Profile'>
        <b:includable id='main' var='this'>
          <!-- Remove widget title -->
          <b:include name='content'/>
        </b:includable>
        <b:includable id='teamProfileLink'>
          <!-- Remove background image, add "Visit profile" message -->
          <a class='profile-link g-profile' expr:href='data:userUrl'>
            <b:include name='profileImage'/>
            <div class='profile-name-wrapper'>
              <div class='profile-name'><data:display-name/></div>
              <div class='visit-profile'><data:messages.visitProfile/></div>
            </div>
          </a>
        </b:includable>
        <b:includable id='viewProfileLink'>
          <!-- Change message to "Visit profile" -->
          <a class='profile-link' expr:href='data:userUrl' rel='author'>
            <data:messages.visitProfile/>
          </a>
        </b:includable>
        <b:includable id='defaultProfileImage'>
          <div class='default-avatar-wrapper'>
            <b:include data='{ iconClass: &quot;avatar-icon&quot; }' name='defaultAvatarIcon'/>
          </div>
        </b:includable>
      </b:defaultmarkup>
    </b:defaultmarkups>
    <b:if cond='data:widgets any (w =&gt; w.type == &quot;AdSense&quot;) or data:blog.adsenseClientId'>
      <script async='async' src='//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'/>
    </b:if>
    <script async='async' src='https://www.gstatic.com/external_hosted/imagesloaded/imagesloaded-3.1.8.min.js'/>
    <script async='async' src='https://www.gstatic.com/external_hosted/vanillamasonry-v3_1_5/masonry.pkgd.min.js'/>
    <script async='async' src='https://www.gstatic.com/external_hosted/clipboardjs/clipboard.min.js'/>
    <b:include data='blog' name='google-analytics'/>

    <b:include cond='not data:view.isPreview' data='{                         image: data:skin.vars.body_background.image,                         selector: &quot;body.homepage-view .hero-image.has-image&quot;,                         imageSizes: [320, 640, 800, 1024, 1440, 1680, 1920, 2560]                      }' name='responsiveImageStyle'/>
  </head>
  <body>
    <b:class cond='data:view.isPreview' name='preview'/>
    <b:class cond='data:view.isHomepage' name='homepage-view'/>
    <b:class cond='data:view.isArchive' name='archive-view'/>
    <b:class cond='data:view.isLabelSearch' name='label-view'/>
    <b:class cond='data:view.isSearch and !data:view.isLabelSearch' name='search-view'/>
    <b:class cond='data:view.isPost' name='post-view'/>
    <b:class cond='data:view.isPage' name='page-view'/>
    <b:class cond='data:view.isMultipleItems' name='feed-view'/>
    <b:class cond='data:view.isSingleItem' name='item-view'/>
    <b:class name='version-1-3-0'/>
    <b:include name='skipNavigation'/>
    <div class='page'>
      <div class='page_body'>
        <div class='main-page-body-content'>
          <div class='centered-top-placeholder'/>
          <header class='centered-top-container' role='banner'>
            <div class='centered-top'>
              <b:class cond='data:view.isSearch and data:view.search.query' name='search-focused'/>
              <b:if cond='data:view.isPost'>
                <div class='back-button-container'>
                  <a expr:href='data:blog.homepageUrl'>
                    <b:include data='{ iconClass: &quot;touch-icon back-button rtl-reversible-icon&quot; }' name='backArrowIcon'/>
                  </a>
                </div>
              <b:else/>
                <div class='hamburger-menu-container'>
                  <b:include data='{ iconClass: &quot;touch-icon hamburger-menu&quot; }' name='menuIcon'/>
                </div>
              </b:if>
              <b:if cond='data:view.isLayoutMode or data:widgets any (w =&gt; w.sectionId == &quot;subscription&quot;)'>
                <section class='subscribe-section-container'>
                  <button class='subscribe-button'><b:eval expr='data:messages.subscribe'/></button>
                  <div class='subscribe-popup-container'>
                    <div aria-labelledby='subscribe-title' class='subscribe-popup dialog hidden' role='dialog' tabindex='-1'>
                      <div role='document'>
                        <h3 class='subscribe-title' id='subscribe-title'><b:eval expr='data:messages.subscribeToThisBlog'/></h3>
                        <b:section id='subscription' name='Subscription' showaddelement='false'>
                          <b:widget id='FollowByEmail1' locked='true' title='Follow by Email' type='FollowByEmail' visible='false'>
                            <b:includable id='main'>
  <b:include name='widget-title'/>
  <b:include name='content'/>
</b:includable>
                            <b:includable id='content'>
  <div class='widget-content'>
    <div class='follow-by-email-inner'>
      <form action='https://feedburner.google.com/fb/a/mailverify' expr:onsubmit='&quot;window.open(\&quot;https://feedburner.google.com/fb/a/mailverify?uri=&quot; + data:feedPath + &quot;\&quot;, \&quot;popupwindow\&quot;, \&quot;scrollbars=yes,width=550,height=520\&quot;); return true&quot;' method='post' target='popupwindow'>
        <input autocomplete='off' class='follow-by-email-address' expr:placeholder='data:messages.emailAddress' name='email' type='email'/>
        <input class='follow-by-email-submit' expr:value='data:messages.getEmailNotifications' type='submit'/>
        <input expr:value='data:feedPath' name='uri' type='hidden'/>
        <input name='loc' type='hidden' value='en_US'/>
      </form>
    </div>
  </div>
</b:includable>
                          </b:widget>
                        </b:section>
                      </div>
                    </div>
                  </div>
                </section>
              </b:if>
              <b:if cond='data:view.isLayoutMode or data:widgets any (w =&gt; w.sectionId == &quot;search_top&quot;)'>
                <div class='search'>
                  <b:class cond='data:view.isSearch and data:view.search.query' name='focused'/>
                  <button class='search-expand touch-icon-button' expr:aria-label='data:messages.search.escaped'>
                    <div class='search-expand-text'><data:messages.search/></div>
                    <b:include data='{ iconClass: &quot;touch-icon search-expand-icon&quot; }' name='searchIcon'/>
                  </button>
                  <b:section id='search_top' name='Search (Top)' showaddelement='false'>
                    <b:widget id='BlogSearch1' locked='true' title='Search This Blog' type='BlogSearch' visible='true'>
                      <b:includable id='main'>
  <b:include name='widget-title'/>
  <b:include name='content'/>
</b:includable>
                      <b:includable id='content'>
  <div class='widget-content' role='search'>
    <b:include name='searchForm'/>
  </div>
</b:includable>
                      <b:includable id='searchForm'>
  <form expr:action='data:blog.searchUrl'>
    <b:attr cond='not data:view.isPreview' name='target' value='_top'/>
    <b:include name='urlParamsAsFormInput'/>
    <div class='search-input'>
      <input autocomplete='off' expr:aria-label='data:messages.searchThisBlog' expr:placeholder='data:messages.searchThisBlog' expr:value='data:view.isSearch ? data:view.search.query.escaped : &quot;&quot;' name='q'/>
    </div>
    <b:include name='searchSubmit'/>
  </form>
</b:includable>
                      <b:includable id='searchSubmit'>
          <b:if cond='data:widget.sectionId == &quot;search_top&quot;'>
            <label>
              <input type='submit'/>
              <b:include data='{ iconClass: &quot;touch-icon search-icon&quot; }' name='searchIcon'/>
            </label>
          <b:else/>
            <b:include name='super.searchSubmit'/>
          </b:if>
        </b:includable>
                    </b:widget>
                  </b:section>
                </div>
              </b:if>
              <div class='blog-name'>
                <b:section id='header' name='Header' showaddelement='false'>
                  <b:widget id='Header1' locked='true' title='SOE THU (Header)' type='Header' visible='true'>
                    <b:widget-settings>
                      <b:widget-setting name='displayUrl'/>
                      <b:widget-setting name='displayHeight'>0</b:widget-setting>
                      <b:widget-setting name='sectionWidth'>-1</b:widget-setting>
                      <b:widget-setting name='useImage'>false</b:widget-setting>
                      <b:widget-setting name='shrinkToFit'>false</b:widget-setting>
                      <b:widget-setting name='imagePlacement'>BEHIND</b:widget-setting>
                      <b:widget-setting name='displayWidth'>0</b:widget-setting>
                    </b:widget-settings>
                    <b:includable id='main' var='this'>
    <div class='header-widget'>
      <b:include cond='data:imagePlacement in {&quot;REPLACE&quot;, &quot;BEFORE_DESCRIPTION&quot;}' name='image'/>
      <b:include cond='data:imagePlacement not in {&quot;REPLACE&quot;, &quot;BEFORE_DESCRIPTION&quot;}' name='title'/>
      <b:include cond='data:imagePlacement != &quot;REPLACE&quot;' name='description'/>
    </div>
    <b:include cond='data:imagePlacement == &quot;BEHIND&quot;' name='behindImageStyle'/>
  </b:includable>
                    <b:includable id='behindImageStyle'>
    <b:if cond='data:sourceUrl'>
      <b:include cond='data:this.image' data='{                    image: data:this.image,                    selector: &quot;.header-widget&quot;                  }' name='responsiveImageStyle'/>
      <style type='text/css'>
        .header-widget {
          background-position: <data:blog.locale.languageAlignment/>;
          background-repeat: no-repeat;
        }
      </style>
    </b:if>
  </b:includable>
                    <b:includable id='description'>
    <p>
      <data:this.description/>
    </p>
  </b:includable>
                    <b:includable id='image'>
          <b:include name='super.image'/>
          <!-- If we are replacing the title, force it to render anyway, and it'll be hidden in CSS. -->
          <b:include cond='data:this.imagePlacement == &quot;REPLACE&quot;' name='title'/>
        </b:includable>
                    <b:includable id='title'>
          <div>
            <b:class cond='data:this.imagePlacement == &quot;REPLACE&quot;' name='replaced'/>
            <b:include name='super.title'/>
          </div>
        </b:includable>
                  </b:widget>
                </b:section>
                <nav role='navigation'>
                  <b:section id='page_list_top' name='Page List (Top)' showaddelement='false'>
                    <b:widget id='PageList1' locked='true' title='Pages' type='PageList' visible='false'>
                      <b:widget-settings>
                        <b:widget-setting name='pageListJson'><![CDATA[{'home': {'href': 'https://openlyayemyaing.blogspot.com/', 'title': 'Home', 'position': 0}}]]></b:widget-setting>
                        <b:widget-setting name='homeTitle'>Home</b:widget-setting>
                      </b:widget-settings>
                      <b:includable id='main'>
  <b:include name='widget-title'/>
  <b:include name='content'/>
</b:includable>
                      <b:includable id='content'>
          <div class='widget-content'>
            <b:if cond='data:widget.sectionId == &quot;page_list_top&quot;'>
              <b:include name='overflowablePageList'/>
            <b:else/>
              <b:include name='pageList'/>
            </b:if>
          </div>
        </b:includable>
                      <b:includable id='overflowButton'>
          <a><data:messages.moreEllipsis/></a>
        </b:includable>
                      <b:includable id='overflowablePageList'>
  <div class='overflowable-container'>
    <div class='overflowable-contents'>
      <div class='container'>
        <b:with value='true' var='overflow'>
        <b:with value='&quot;tabs&quot;' var='pageListClass'>
          <b:include name='pageList'/>
        </b:with>
        </b:with>
      </div>
    </div>
    <div class='overflow-button hidden'>
      <b:include name='overflowButton'/>
    </div>
  </div>
</b:includable>
                      <b:includable id='pageLink'>
  <li>
    <b:class cond='data:overflow' name='overflowable-item'/>
    <b:class cond='data:link.isCurrentPage' name='selected'/>

    <a expr:href='data:link.href'><data:link.title/></a>
  </li>
</b:includable>
                      <b:includable id='pageList'>
  <ul>
    <b:class cond='data:pageListClass' expr:name='data:pageListClass'/>
    <b:loop values='data:links' var='link'>
      <b:include name='pageLink'/>
    </b:loop>
  </ul>
</b:includable>
                    </b:widget>
                  </b:section>
                </nav>
              </div>
            </div>
          </header>
          <div class='hero-image'>
            <b:class cond='data:skin.vars.body_background.image' name='has-image'/>
          </div>
          <main class='centered-bottom' id='main' role='main' tabindex='-1'>
            <b:if cond='data:view.isMultipleItems'>
              <h2 class='main-heading'><data:messages.posts/></h2>
            </b:if>
            <b:if cond='data:view.isArchive or (data:view.isSearch and data:view.search.resultsMessageHtml)'>
              <div class='post-filter-message'>
                <div class='message-container'>
                  <b:if cond='data:view.isArchive'>
                    <data:view.archive.rangeMessage/>
                  <b:elseif cond='data:view.isSearch and data:view.search.resultsMessageHtml'/>
                    <data:view.search.resultsMessageHtml/>
                  </b:if>
                </div>
                <div class='home-link-container'>
                  <a class='home-link' expr:href='data:blog.homepageUrl'><data:messages.showAll/></a>
                </div>
              </div>
            </b:if>
            <b:section ads='true' class='main' id='page_body' name='Page Body' showaddelement='false'>
              <b:widget cond='data:view.isHomepage' id='FeaturedPost1' locked='true' title='' type='FeaturedPost' visible='true'>
                <b:widget-settings>
                  <b:widget-setting name='showSnippet'>true</b:widget-setting>
                  <b:widget-setting name='showPostTitle'>true</b:widget-setting>
                  <b:widget-setting name='showFirstImage'>true</b:widget-setting>
                  <b:widget-setting name='useMostRecentPost'>true</b:widget-setting>
                </b:widget-settings>
                <b:includable id='main'>
          <b:with value='data:messages.featured' var='defaultTitle'>
            <b:include name='super.main'/>
          </b:with>
        </b:includable>
                <b:includable id='emailPostIcon'>
          <!-- Replace icon with text -->
          <span class='byline'>
            <a class='flat-button' expr:href='data:post.emailPostUrl'><data:messages.emailPost/></a>
          </span>
        </b:includable>
                <b:includable id='footerBylines'>
          <b:if cond='data:view.isSingleItem and data:widget.type == &quot;Blog&quot;'>
            <b:include name='super.footerBylines'/>
          <b:else/>
            <b:include data='{ items: [[&quot;share&quot;, &quot;comments&quot;]] }' name='footerBylinesOverride'/>
          </b:if>
        </b:includable>
                <b:includable id='headerByline'>
          <b:if cond='data:view.isSingleItem and data:widget.type == &quot;Blog&quot;'>
            <b:include name='super.headerByline'/>
          <b:else/>
            <b:include data='{ items: [&quot;author&quot;, &quot;timestamp&quot;] }' name='headerBylineOverride'/>
          </b:if>
        </b:includable>
                <b:includable id='postLabels'>
          <b:include cond='data:view.isSingleItem and data:widget.type == &quot;Blog&quot;' name='super.postLabels'/>
        </b:includable>
                <b:includable id='sharingButtonContent'>
          <b:message name='messages.share'/>
        </b:includable>
                <b:includable id='snippetedPostByline' var='post'>
          <b:include name='headerByline'/>
        </b:includable>
                <b:includable id='snippetedPostContent'>
          <b:with value='data:postDisplay.showFeaturedImage and data:post.featuredImage' var='hasImage'>
            <div class='post-content'>
              <b:class cond='data:hasImage' name='has-featured-image'/>
              <b:class cond='not data:hasImage' name='no-featured-image'/>

              <!-- Change the order and add a snippet container -->
              <b:include cond='data:hasImage' data='post' name='snippetedPostThumbnail'/>
              <div class='post-text-container'>
                <b:include name='headerByline'/>
                <b:include cond='data:this.postDisplay.showTitle' name='snippetedPostTitle'/>
                <b:with value='&quot;featured-post&quot;' var='snippetPrefix'>
                  <b:include cond='data:this.postDisplay.showSnippet' data='post' name='postSnippet'/>
                </b:with>
                <div class='post-footer'>
                  <b:include name='footerBylines'/>
                  <b:include data='post' name='postJumpLink'/>
                </div>
              </div>
            </div>
          </b:with>
        </b:includable>
                <b:includable id='snippetedPostThumbnail'>
          <b:include data='{image: data:featuredImage, maxSize: 954, selector: &quot;.hero-thumb&quot;}' name='responsiveImageStyle'/>
          <a class='thumb-link' expr:href='data:post.url'><div class='thumb hero-thumb'/></a>
        </b:includable>
              </b:widget>
              <b:widget cond='data:view.isHomepage' id='AdSense1' locked='false' title='' type='AdSense' visible='false'>
                <b:includable id='main'>
  <div class='widget-content'>
    <b:if cond='data:adCode'>
      <data:adCode/>
    <b:else/>
      <b:include name='defaultAdUnit'/>
    </b:if>
  </div>
</b:includable>
                <b:includable id='defaultAdUnit'>
          <!-- Clear out style (need non-empty string) -->
          <b:with value='&quot;/* Done in css. */&quot;' var='style'>
            <b:include name='super.defaultAdUnit'/>
          </b:with>
        </b:includable>
              </b:widget>
              <b:widget id='Blog1' locked='true' title='Blog Posts' type='Blog' visible='true'>
                <b:widget-settings>
                  <b:widget-setting name='showDateHeader'>false</b:widget-setting>
                  <b:widget-setting name='style.textcolor'>#000000</b:widget-setting>
                  <b:widget-setting name='showShareButtons'>true</b:widget-setting>
                  <b:widget-setting name='showCommentLink'>true</b:widget-setting>
                  <b:widget-setting name='style.urlcolor'>#000000</b:widget-setting>
                  <b:widget-setting name='showAuthor'>false</b:widget-setting>
                  <b:widget-setting name='disableGooglePlusShare'>true</b:widget-setting>
                  <b:widget-setting name='style.linkcolor'>#01050c</b:widget-setting>
                  <b:widget-setting name='style.unittype'>TextAndImage</b:widget-setting>
                  <b:widget-setting name='style.bgcolor'>#ffffff</b:widget-setting>
                  <b:widget-setting name='timestampLabel'/>
                  <b:widget-setting name='showAuthorProfile'>false</b:widget-setting>
                  <b:widget-setting name='style.layout'>1x1</b:widget-setting>
                  <b:widget-setting name='showLabels'>true</b:widget-setting>
                  <b:widget-setting name='showLocation'>true</b:widget-setting>
                  <b:widget-setting name='showTimestamp'>true</b:widget-setting>
                  <b:widget-setting name='postsPerAd'>1</b:widget-setting>
                  <b:widget-setting name='showBacklinks'>false</b:widget-setting>
                  <b:widget-setting name='style.bordercolor'>#ffffff</b:widget-setting>
                  <b:widget-setting name='showInlineAds'>false</b:widget-setting>
                  <b:widget-setting name='showReactions'>false</b:widget-setting>
                </b:widget-settings>
                <b:includable id='main'>
          <b:if cond='not data:posts.any'>
            <div class='no-posts'>
              <b:eval expr='data:view.isSearch ? data:messages.noResultsFound : data:messages.theresNothingHere'/>
            </div>
          </b:if>

          <!-- Display title on homepage -->
          <b:if cond='data:posts.any and data:view.isHomepage'>
            <h3 class='title'><data:messages.latestPosts/></h3>
          </b:if>
          <!-- Filter out the featured post, but only on the homepage. -->
          <b:with value='(data:widgets.FeaturedPost filter w =&gt; w.sectionId == &quot;page_body&quot;) map (w =&gt; w.postId)' var='featuredPostIds'>
            <b:with value='data:view.isHomepage ? data:posts filter (post =&gt; post.id not in data:featuredPostIds) : data:posts' var='posts'>
              <b:include name='super.main'/>
            </b:with>
          </b:with>
        </b:includable>
                <b:includable id='aboutPostAuthor'>
  <div class='author-name'>
    <a class='g-profile' expr:href='data:post.author.profileUrl' rel='author' title='author profile'>
      <span>
        <data:post.author.name/>
      </span>
    </a>
  </div>
  <div>
    <span class='author-desc'>
      <data:post.author.aboutMe/>
    </span>
  </div>
</b:includable>
                <b:includable id='addComments'>
  <a expr:href='data:post.commentsUrl' expr:onclick='data:post.commentsUrlOnclick'>
    <b:message name='messages.postAComment'/>
  </a>
</b:includable>
                <b:includable id='commentAuthorAvatar'>
  <div class='avatar-image-container'>
    <img class='author-avatar' expr:src='data:comment.authorAvatarSrc' height='35' width='35'/>
  </div>
</b:includable>
                <b:includable id='commentDeleteIcon' var='comment'>
  <span expr:class='&quot;item-control &quot; + data:comment.adminClass'>
    <b:if cond='data:showCmtPopup'>
      <div class='goog-toggle-button'>
        <div class='goog-inline-block comment-action-icon'/>
      </div>
    <b:else/>
      <a class='comment-delete' expr:href='data:comment.deleteUrl' expr:title='data:messages.deleteComment'>
        <img src='https://resources.blogblog.com/img/icon_delete13.gif'/>
      </a>
    </b:if>
  </span>
</b:includable>
                <b:includable id='commentForm' var='post'>
  <div class='comment-form'>
    <a name='comment-form'/>
    <h4 id='comment-post-message'><data:messages.postAComment/></h4>
    <b:if cond='data:this.messages.blogComment != &quot;&quot;'>
      <p><data:this.messages.blogComment/></p>
    </b:if>
    <b:include data='post' name='commentFormIframeSrc'/>
    <iframe allowtransparency='allowtransparency' class='blogger-iframe-colorize blogger-comment-from-post' expr:height='data:cmtIframeInitialHeight ?: &quot;90px&quot;' frameborder='0' id='comment-editor' name='comment-editor' src='' width='100%'/>
    <data:post.cmtfpIframe/>
    <script type='text/javascript'>
      BLOG_CMT_createIframe(&#39;<data:post.appRpcRelayPath/>&#39;);
    </script>
  </div>
</b:includable>
                <b:includable id='commentFormIframeSrc' var='post'>
  <a expr:href='data:post.commentFormIframeSrc' id='comment-editor-src'/>
</b:includable>
                <b:includable id='commentItem' var='comment'>
  <div class='comment' expr:id='&quot;c&quot; + data:comment.id'>
    <b:include cond='data:blog.enabledCommentProfileImages' name='commentAuthorAvatar'/>

    <div class='comment-block'>
      <div class='comment-author'>
        <b:if cond='data:comment.authorUrl'>
          <b:message name='messages.authorSaidWithLink'>
            <b:param expr:value='data:comment.author' name='authorName'/>
            <b:param expr:value='data:comment.authorUrl' name='authorUrl'/>
          </b:message>
        <b:else/>
          <b:message name='messages.authorSaid'>
            <b:param expr:value='data:comment.author' name='authorName'/>
          </b:message>
        </b:if>
      </div>
      <div expr:class='&quot;comment-body&quot; + (data:comment.isDeleted ? &quot; deleted&quot; : &quot;&quot;)'>
        <data:comment.body/>
      </div>
      <div class='comment-footer'>
        <span class='comment-timestamp'>
          <a expr:href='data:comment.url' title='comment permalink'>
            <data:comment.timestamp/>
          </a>
          <b:include data='comment' name='commentDeleteIcon'/>
        </span>
      </div>
    </div>
  </div>
</b:includable>
                <b:includable id='commentList' var='comments'>
  <div id='comments-block'>
    <b:loop values='data:comments' var='comment'>
      <b:include data='comment' name='commentItem'/>
    </b:loop>
  </div>
</b:includable>
                <b:includable id='commentPicker' var='post'>
  <b:if cond='data:post.commentSource == 1'>
    <b:include data='post' name='iframeComments'/>
  <b:elseif cond='data:post.showThreadedComments'/>
    <b:include data='post' name='threadedComments'/>
  <b:else/>
    <b:include data='post' name='comments'/>
  </b:if>
</b:includable>
                <b:includable id='comments' var='post'>
  <section expr:class='&quot;comments&quot; + (data:post.embedCommentForm ? &quot; embed&quot; : &quot;&quot;)' expr:data-num-comments='data:post.numberOfComments' id='comments'>
    <a name='comments'/>
    <b:if cond='data:post.allowComments'>

      <b:include name='commentsTitle'/>

      <div expr:id='data:widget.instanceId + &quot;_comments-block-wrapper&quot;'>
        <b:include cond='data:post.comments' data='post.comments' name='commentList'/>
      </div>

      <b:if cond='data:post.commentPagingRequired'>
        <div class='paging-control-container'>
          <b:if cond='data:post.hasOlderLinks'>
            <a expr:class='data:post.oldLinkClass' expr:href='data:post.oldestLinkUrl'>
              <data:messages.oldest/>
            </a>
            <a expr:class='data:post.oldLinkClass' expr:href='data:post.olderLinkUrl'>
              <data:messages.older/>
            </a>
          </b:if>

          <span class='comment-range-text'>
            <data:post.commentRangeText/>
          </span>

          <b:if cond='data:post.hasNewerLinks'>
            <a expr:class='data:post.newLinkClass' expr:href='data:post.newerLinkUrl'>
              <data:messages.newer/>
            </a>
            <a expr:class='data:post.newLinkClass' expr:href='data:post.newestLinkUrl'>
              <data:messages.newest/>
            </a>
          </b:if>
        </div>
      </b:if>

      <div class='footer'>
        <b:if cond='data:post.embedCommentForm'>
          <b:if cond='data:post.allowNewComments'>
            <b:include data='post' name='commentForm'/>
          <b:else/>
            <data:post.noNewCommentsText/>
          </b:if>
        <b:else/>
          <b:if cond='data:post.allowComments'>
            <b:include data='post' name='addComments'/>
          </b:if>
        </b:if>
      </div>
    </b:if>
    <b:if cond='data:showCmtPopup'>
      <div id='comment-popup'>
        <iframe allowtransparency='allowtransparency' frameborder='0' id='comment-actions' name='comment-actions' scrolling='no'>
        </iframe>
      </div>
    </b:if>
  </section>
</b:includable>
                <b:includable id='commentsTitle'>
  <h3 class='title'><data:messages.comments/></h3>
</b:includable>
                <b:includable id='defaultAdUnit'>
          <!-- Clear out style (need non-empty string) -->
          <b:with value='&quot;/* Done in css. */&quot;' var='style'>
            <b:include name='super.defaultAdUnit'/>
          </b:with>
        </b:includable>
                <b:includable id='emailPostIcon'>
          <!-- Replace icon with text -->
          <span class='byline'>
            <a class='flat-button' expr:href='data:post.emailPostUrl'><data:messages.emailPost/></a>
          </span>
        </b:includable>
                <b:includable id='feedLinks'>
          <!-- Don't render -->
        </b:includable>
                <b:includable id='feedLinksBody' var='links'>
  <div class='feed-links'>
  <data:messages.subscribeTo/>
  <b:loop values='data:links' var='f'>
     <a class='feed-link' expr:href='data:f.url' expr:type='data:f.mimeType' target='_blank'><data:f.name/> (<data:f.feedType/>)</a>
  </b:loop>
  </div>
</b:includable>
                <b:includable id='footerBylines'>
          <b:if cond='data:view.isSingleItem and data:widget.type == &quot;Blog&quot;'>
            <b:include name='super.footerBylines'/>
          <b:else/>
            <b:include data='{ items: [[&quot;share&quot;, &quot;comments&quot;]] }' name='footerBylinesOverride'/>
          </b:if>
        </b:includable>
                <b:includable id='headerByline'>
          <b:if cond='data:view.isSingleItem and data:widget.type == &quot;Blog&quot;'>
            <b:include name='super.headerByline'/>
          <b:else/>
            <b:include data='{ items: [&quot;author&quot;, &quot;timestamp&quot;] }' name='headerBylineOverride'/>
          </b:if>
        </b:includable>
                <b:includable id='homePageLink'>
  <a class='home-link' expr:href='data:blog.homepageUrl'>
    <data:messages.home/>
  </a>
</b:includable>
                <b:includable id='iframeComments' var='post'>
  <b:if cond='data:post.allowIframeComments'>
    <script expr:src='data:post.iframeCommentSrc' type='text/javascript'/>
    <div class='cmt_iframe_holder' expr:data-href='data:post.url.canonical' expr:data-viewtype='data:post.viewType'/>

    <b:if cond='!data:post.embedCommentForm'>
      <b:include data='post' name='commentsLink'/>
    </b:if>
  </b:if>
</b:includable>
                <b:includable id='inlineAd' var='post'>
  <b:if cond='!data:view.isPreview'>
    <b:if cond='data:this.adCode or data:this.adClientId or data:blog.adsenseClientId'>
      <!-- Ad -->
      <div class='inline-ad'>
        <b:if cond='data:this.adCode != &quot;&quot;'>
          <data:this.adCode/>
        <b:else/>
          <b:include cond='data:this.adClientId or data:blog.adsenseClientId' name='defaultAdUnit'/>
        </b:if>
      </div>
    </b:if>
  <b:else/>
    <div class='inline-ad'>
      <div class='inline-ad-placeholder'>
        <span><b:message name='messages.adsGoHere'/></span>
      </div>
    </div>
  </b:if>
</b:includable>
                <b:includable id='nextPageLink'>
  <a class='blog-pager-older-link' expr:href='data:olderPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-older-link&quot;' expr:title='data:messages.olderPosts'>
    <data:messages.olderPosts/>
  </a>
</b:includable>
                <b:includable id='post' var='post'>
          <b:if cond='data:view.isSingleItem'>
            <div class='post-sidebar'>
              <b:if cond='data:widgets.Blog.first.allBylineItems.share and data:post.shareUrl'>
                <div class='post-sidebar-item post-share-buttons'>
                  <b:with value='data:widget.instanceId + &quot;-&quot; + (data:regionName ?: &quot;byline&quot;) + &quot;-&quot; + data:post.id' var='sharingId'>
                    <b:include data='{                                                              sharingId: data:sharingId,                                                              originalUrl: data:post.url,                                                              shareUrl: data:post.shareUrl,                                                              platforms: data:blog.sharing.platforms,                                                            }' name='sharingButtons'/>
                  </b:with>
                </div>
              </b:if>
              <b:if cond='data:widgets.Blog.first.allBylineItems.labels and data:post.labels'>
                <div class='post-sidebar-item post-sidebar-labels'>
                  <div><data:messages.labels/></div>
                  <ul>
                    <b:loop index='i' values='data:post.labels' var='label'>
                      <li><a expr:href='data:label.url' rel='tag'><data:label.name/></a></li>
                    </b:loop>
                  </ul>
                </div>
              </b:if>
            </div>
          </b:if>
          <div class='post'>
            <b:class cond='data:view.isMultipleItems and data:post.featuredImage' name='has-featured-image'/>
            <b:class cond='data:view.isMultipleItems and not data:post.featuredImage' name='no-featured-image'/>
            <b:include data='post' name='postMeta'/>
            <b:if cond='data:view.isSingleItem'>
              <b:include name='headerByline'/>
              <b:include data='post' name='postTitle'/>
              <div class='post-body-container'>
                <b:include data='post' name='postBody'/>
              </div>
            <b:else/>
              <b:if cond='data:post.featuredImage'>
                <div class='snippet-thumbnail'>
                  <a expr:href='data:post.url'>
                    <b:comment>Max width is 576, so max size @ 2x is 1152.</b:comment>
                    <b:include data='{                                        image: data:post.featuredImage,                                        imageSizes: [320,490,576,1152],                                        sourceSizes: &quot;(max-width: 576px) 100vw, (max-width: 1024px) 576px, 490px&quot;                                      }' name='responsiveImage'/>
                  </a>
                  <b:include name='headerByline'/>
                </div>
              <b:else/>
                <b:include name='headerByline'/>
              </b:if>
              <b:include data='post' name='postTitle'/>
            </b:if>
            <b:include data='post' name='postFooter'/>
          </div>
        </b:includable>
                <b:includable id='postBody' var='post'>
  <!-- If metaDescription is empty, use the post body as the schema.org description too, for G+/FB snippeting. -->
  <div class='post-body entry-content float-container' expr:id='&quot;post-body-&quot; + data:post.id'>
    <data:post.body/>
  </div>
</b:includable>
                <b:includable id='postBodySnippet' var='post'>
  <b:include data='post' name='postBody'/>
</b:includable>
                <b:includable id='postCommentsAndAd' var='post'>
          <!-- Always render inline ad inside container -->
          <div class='post-outer-container'>
            <div class='post-outer'>
              <b:include data='post' name='post'/>
            </div>
            <b:include cond='data:view.isSingleItem' data='post' name='commentPicker'/>
            <b:include cond='data:post.includeAd and data:post.adNumber lt (data:view.isHomepage ? 2 : 3)' data='post' name='inlineAd'/>
          </div>
        </b:includable>
                <b:includable id='postCommentsLink'>
  <b:if cond='data:view.isMultipleItems'>
    <span class='byline post-comment-link container'>
      <b:include cond='data:post.commentSource != 1' name='commentsLink'/>
      <b:include cond='data:post.commentSource == 1' name='commentsLinkIframe'/>
    </span>
  </b:if>
</b:includable>
                <b:includable id='postFooter' var='post'>
  <div class='post-footer'>
    <b:include name='footerBylines'/>
    <b:include data='post' name='postFooterAuthorProfile'/>
  </div>
</b:includable>
                <b:includable id='postFooterAuthorProfile' var='post'>
  <b:if cond='data:post.author.aboutMe and data:view.isPost'>
    <div class='author-profile'>
      <b:if cond='data:post.author.authorPhoto.url'>
        <img class='author-image' expr:src='data:post.author.authorPhoto.url' width='50px'/>
        <div class='author-about'>
          <b:include data='post' name='aboutPostAuthor'/>
        </div>
      <b:else/>
        <b:include data='post' name='aboutPostAuthor'/>
      </b:if>
    </div>
  </b:if>
</b:includable>
                <b:includable id='postHeader' var='post'>
  <b:include name='headerByline'/>
</b:includable>
                <b:includable id='postLabels'>
          <b:include cond='data:view.isSingleItem and data:widget.type == &quot;Blog&quot;' name='super.postLabels'/>
        </b:includable>
                <b:includable id='postMeta' var='post'>
  <b:include data='post' name='postMetadataJSON'/>
</b:includable>
                <b:includable id='postPagination'>
  <div class='blog-pager container' id='blog-pager'>
    <b:include cond='data:newerPageUrl' name='previousPageLink'/>
    <b:include cond='data:olderPageUrl' name='nextPageLink'/>
    <b:include cond='data:view.url != data:blog.homepageUrl' name='homePageLink'/>
  </div>
</b:includable>
                <b:includable id='postTitle' var='post'>
  <a expr:name='data:post.id'/>
  <b:if cond='data:post.title != &quot;&quot;'>
    <h3 class='post-title entry-title'>
      <b:if cond='data:post.link or (data:post.url and data:view.url != data:post.url)'>
        <a expr:href='data:post.link ?: data:post.url'><data:post.title/></a>
      <b:else/>
        <data:post.title/>
      </b:if>
    </h3>
  </b:if>
</b:includable>
                <b:includable id='previousPageLink'>
  <a class='blog-pager-newer-link' expr:href='data:newerPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-newer-link&quot;' expr:title='data:messages.newerPosts'>
    <data:messages.newerPosts/>
  </a>
</b:includable>
                <b:includable id='sharingButtonContent'>
          <b:message name='messages.share'/>
        </b:includable>
                <b:includable id='threadedCommentForm' var='post'>
  <div class='comment-form'>
    <a name='comment-form'/>
    <h4 id='comment-post-message'><data:messages.postAComment/></h4>
    <b:if cond='data:this.messages.blogComment != &quot;&quot;'>
      <p><data:this.messages.blogComment/></p>
    </b:if>
    <b:include data='post' name='commentFormIframeSrc'/>
    <iframe allowtransparency='allowtransparency' class='blogger-iframe-colorize blogger-comment-from-post' expr:height='data:cmtIframeInitialHeight ?: &quot;90px&quot;' frameborder='0' id='comment-editor' name='comment-editor' src='' width='100%'/>
    <data:post.cmtfpIframe/>
    <script type='text/javascript'>
      BLOG_CMT_createIframe(&#39;<data:post.appRpcRelayPath/>&#39;);
    </script>
  </div>
</b:includable>
                <b:includable id='threadedCommentJs' var='post'>
  <script async='async' expr:src='data:post.commentSrc' type='text/javascript'/>
  <b:template-script inline='true' name='threaded_comments'/>
  <script type='text/javascript'>
    blogger.widgets.blog.initThreadedComments(
        <data:post.commentJso/>,
        <data:post.commentMsgs/>,
        <data:post.commentConfig/>);
  </script>
</b:includable>
                <b:includable id='threadedComments' var='post'>
  <section class='comments threaded' expr:data-embed='data:post.embedCommentForm' expr:data-num-comments='data:post.numberOfComments' id='comments'>
    <a name='comments'/>

    <b:include name='commentsTitle'/>

    <div class='comments-content'>
      <b:if cond='data:post.embedCommentForm'>
        <b:include data='post' name='threadedCommentJs'/>
      </b:if>
      <div id='comment-holder'>
         <data:post.commentHtml/>
      </div>
    </div>

    <p class='comment-footer'>
      <b:if cond='data:post.allowNewComments'>
        <b:include data='post' name='threadedCommentForm'/>
      <b:else/>
        <data:post.noNewCommentsText/>
      </b:if>
    </p>

    <b:if cond='data:showCmtPopup'>
      <div id='comment-popup'>
        <iframe allowtransparency='allowtransparency' frameborder='0' id='comment-actions' name='comment-actions' scrolling='no'>
        </iframe>
      </div>
    </b:if>
  </section>
</b:includable>
              </b:widget>
              <b:widget cond='data:view.isSingleItem and data:posts any (p =&gt; p.id != data:view.postId)' id='PopularPosts1' locked='true' title='' type='PopularPosts' visible='true'>
                <b:widget-settings>
                  <b:widget-setting name='numItemsToShow'>2</b:widget-setting>
                  <b:widget-setting name='showThumbnails'>true</b:widget-setting>
                  <b:widget-setting name='showSnippets'>true</b:widget-setting>
                  <b:widget-setting name='timeRange'>LAST_YEAR</b:widget-setting>
                </b:widget-settings>
                <b:includable id='main'>
          <!-- Default the title to 'Popular posts'. -->
          <b:with value='data:messages.popularPosts' var='defaultTitle'>
            <b:include name='super.main'/>
          </b:with>
        </b:includable>
                <b:includable id='emailPostIcon'>
          <!-- Replace icon with text -->
          <span class='byline'>
            <a class='flat-button' expr:href='data:post.emailPostUrl'><data:messages.emailPost/></a>
          </span>
        </b:includable>
                <b:includable id='footerBylines'>
          <b:if cond='data:view.isSingleItem and data:widget.type == &quot;Blog&quot;'>
            <b:include name='super.footerBylines'/>
          <b:else/>
            <b:include data='{ items: [[&quot;share&quot;, &quot;comments&quot;]] }' name='footerBylinesOverride'/>
          </b:if>
        </b:includable>
                <b:includable id='headerByline'>
          <b:if cond='data:view.isSingleItem and data:widget.type == &quot;Blog&quot;'>
            <b:include name='super.headerByline'/>
          <b:else/>
            <b:include data='{ items: [&quot;author&quot;, &quot;timestamp&quot;] }' name='headerBylineOverride'/>
          </b:if>
        </b:includable>
                <b:includable id='postLabels'>
          <b:include cond='data:view.isSingleItem and data:widget.type == &quot;Blog&quot;' name='super.postLabels'/>
        </b:includable>
                <b:includable id='sharingButtonContent'>
          <b:message name='messages.share'/>
        </b:includable>
                <b:includable id='snippetedPostContent'>
          <div class='post'>
            <b:class cond='data:post.featuredImage' name='has-featured-image'/>
            <b:class cond='not data:post.featuredImage' name='no-featured-image'/>
            <b:if cond='data:post.featuredImage'>
              <div class='snippet-thumbnail'>
                <a expr:href='data:post.url'>
                  <b:include data='{                                      image: data:post.featuredImage,                                      imageSizes: [330,660,1320],                                      sourceSizes: &quot;(max-width: 660px) 100vw, 660px&quot;                                    }' name='responsiveImage'/>
                </a>
                <b:include name='headerByline'/>
              </div>
            <b:else/>
              <b:include name='headerByline'/>
            </b:if>
            <b:include cond='data:this.postDisplay.showTitle' name='snippetedPostTitle'/>
            <div class='post-footer'>
              <b:include name='footerBylines'/>
            </div>
          </div>
        </b:includable>
              </b:widget>
            </b:section>
          </main>
        </div>
        <b:section class='footer' id='footer' name='Footer' showaddelement='false' tag='footer'>
          <b:widget id='Attribution1' locked='true' title='' type='Attribution' visible='true'>
            <b:widget-settings>
              <b:widget-setting name='copyright'>UG</b:widget-setting>
            </b:widget-settings>
            <b:includable id='main' var='this'>
  <div class='widget-content'>
    <div class='blogger'>
      <a expr:href='data:bloggerUrl' rel='nofollow'>
        <b:include name='flatBloggerIcon'/>
        <b:message name='messages.poweredByBlogger'/>
      </a>
    </div>

    <b:if cond='data:imageAuthor'>
      <div class='image-attribution'>
        <b:if cond='data:imageAuthor.url'>
          <b:message name='messages.templateImagesByLink'>
            <b:param expr:value='data:imageAuthor.url'/>
            <b:param expr:value='data:imageAuthor.name'/>
          </b:message>
        <b:else/>
          <b:message name='messages.templateImagesBy'>
            <b:param expr:value='data:imageAuthor.name'/>
          </b:message>
        </b:if>
      </div>
    </b:if>

    <b:if cond='data:copyright != &quot;&quot;'>
      <div class='copyright'><data:copyright/></div>
    </b:if>
  </div>
</b:includable>
          </b:widget>
        </b:section>
      </div>
    </div>
    <aside class='sidebar-container container sidebar-invisible' role='complementary'>
      <div class='navigation'>
        <b:include data='{ iconClass: &quot;touch-icon sidebar-back rtl-reversible-icon&quot; }' name='backArrowIcon'/>
      </div>
      <b:section id='sidebar' name='Sidebar' preferred='yes'>
        <b:widget id='Profile1' locked='false' title='မြန်မာ' type='Profile' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='showaboutme'>true</b:widget-setting>
            <b:widget-setting name='showlocation'>false</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main' var='this'>
          <!-- Remove widget title -->
          <b:include name='content'/>
        </b:includable>
          <b:includable id='authorProfileImage'>
  <img class='profile-img' expr:alt='data:messages.myPhoto' expr:height='data:authorPhoto.height' expr:src='data:authorPhoto.image' expr:width='data:authorPhoto.width'/>
</b:includable>
          <b:includable id='content'>
  <b:if cond='data:team'>
    <div class='widget-content team'>
      <b:include name='teamProfile'/>
    </div>
  <b:else/>
    <div class='widget-content individual'>
      <b:include name='userProfile'/>
    </div>
  </b:if>
</b:includable>
          <b:includable id='defaultProfileImage'>
          <div class='default-avatar-wrapper'>
            <b:include data='{ iconClass: &quot;avatar-icon&quot; }' name='defaultAvatarIcon'/>
          </div>
        </b:includable>
          <b:includable id='profileImage'>
  <b:if cond='data:authorPhoto.image'>
    <b:include name='authorProfileImage'/>
  <b:else/>
    <b:include name='defaultProfileImage'/>
  </b:if>
</b:includable>
          <b:includable id='teamProfile'>
  <ul>
    <b:loop values='data:authors' var='author'>
      <li>
        <div class='team-member'>
          <b:include data='author' name='teamProfileLink'/>
        </div>
      </li>
    </b:loop>
  </ul>
</b:includable>
          <b:includable id='teamProfileLink'>
          <!-- Remove background image, add "Visit profile" message -->
          <a class='profile-link g-profile' expr:href='data:userUrl'>
            <b:include name='profileImage'/>
            <div class='profile-name-wrapper'>
              <div class='profile-name'><data:display-name/></div>
              <div class='visit-profile'><data:messages.visitProfile/></div>
            </div>
          </a>
        </b:includable>
          <b:includable id='userGoogleProfile'>
  <div class='g-follow' data-annotation='bubble' data-height='20' expr:data-href='data:userUrl'/>
</b:includable>
          <b:includable id='userLocation'>
  <dd class='profile-data location'><data:location/></dd>
</b:includable>
          <b:includable id='userProfile'>
  <b:include name='userProfileImage'/>
  <b:include name='userProfileInfo'/>
</b:includable>
          <b:includable id='userProfileData'>
  <dt class='profile-data'>
    <b:include name='userProfileLink'/>
    <b:include cond='data:hasgoogleprofile' name='userGoogleProfile'/>
  </dt>
</b:includable>
          <b:includable id='userProfileImage'>
  <a expr:href='data:userUrl' rel='nof
