#	*Git* and *GitHub* Tutorial

A brief introduction to *Git* and *GitHub* can be found in the
	["Hello World" tutorial](https://guides.github.com/activities/hello-world/)
	\cite{GitHubStaff2016b}, from [GitHub Guides](https://guides.github.com/)
	\cite{GitHubStaff20XY}.

Use *GitHub*, or another Web-based source-code-hosting service, to share your
	portfolio online with other people \cite{Nguyen2014}.
	The portfolio can be used for software development, data science, embedded
		hardware design, VLSI design, UI/UX design, and/or product design.















##	Brief Introduction to *Git*

[*Git* is a free and open source distributed version control system](https://en.wikipedia.org/wiki/Git). You can use it to track different versions/revisions of your projects.

To modify a *Git* repository using the
	[command-line interface](https://en.wikipedia.org/wiki/Command-line_interface) on [*Unix*-like operating systems](https://en.wikipedia.org/wiki/Unix-like) (such as macOS, [GNU/](https://en.wikipedia.org/wiki/GNU/Linux_naming_controversy)[Linux](https://en.wikipedia.org/wiki/Linux), freeBSD, NetBSD, or Open BSD),
	and upload this modification (via `commit` and `push` commands) to my
		server/Web -based *GitHub* repository,
	run the following sequence of commands.
+ `git add -A` (to add file modifications in the repository to this commit)
+ `git commit -m [Descriptive text for this set of file additions/modifications/deletions]` (commit this set of file modifications to the "holding stage," before this set of modifications is pushed/committed to the *GitHub* repository).
+ `git push` (this set of file modifications to the server or Web-based *Git*
		service)



![Git commit and push](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/git-commit-push-files.jpg)



Resources for learning about *Git*:
+ https://www.atlassian.com/git/tutorials
+ https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud






##	Brief Introduction to *GitHub*

The main web page for GitHub is shown below, and is available at: https://github.com/.

![main web page for GitHub](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/github-main-page.jpg)

The main web page for GitHub, after logging in, is shown below.

![main web page for GitHub after logging in](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/github-main-page-logged-in.jpg)




###	Customizing Your *GitHub* Profile

To customize your *GitHub* profile, click on the icon with your profile picture
	and select the ["Settings" option](https://github.com/settings/profile)
	from the drop-down list.

![Drop-down list "Settings" option](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/profile-dropdown-menu-settings.jpg)


You can edit profile information for your *GitHub* account, such as your name, to disclose/display an email address publicly (and if so, which email address) or avoid displaying any email address, a short biography of yourself, the URL of your web page, and your current location.

![Public profile settings](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/profile-settings.jpg)




To change username and password of your *GitHub* profile, select the "Account" option of the menu on the right by clicking on it to go to the ["Account" page](https://github.com/settings/admin).



![To change username and password of your *GitHub* profile](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/change-username-password.jpg)



To change your username for your *GitHub* profile, click on change username. You will be warned about changing your username. Proceed by clicking on the "I understand, let's change my username" option/button.

![Warning about changing your username](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/change-username-2.jpg)

Enter your new username, and click on the "Change my username" option/button.

![Enter your new username.](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/change-username-3.jpg)

The next screen should indicate that your username has been renamed, and it should also show a button to bring you to new profile settings.

![Username has been renamed](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/change-username-4.jpg)



To add and/or change email addresses associated with your *GitHub* profile, [select the "Emails" option of the "Personal settings" menu on the right](https://github.com/settings/emails).


![To add and/or change email addresses associated with your *GitHub* profile](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/change-email.jpg)





###	*GitHub* Repositories

Each project that you work on can be stored locally on your computer, and online with your cloud-based *GitHub* account. To store your project with your *GitHub* account, create and associate a *GitHub* repository to your project. This *GitHub* repository would contain additions, deletions, or modifications of your files associated with that project. For files stored in the *GitHub* repository as [text files (e.g., using the ASCII character set, UTF-8 character encoding, or similar text file formats)](https://en.wikipedia.org/wiki/Text_file), each commit/modification pushed to your *GitHub* repository would show the differences between the files in the current commit/version and the previous commit/version (if they exist).








###	Creating A New *GitHub* Repository

To create a new *GitHub* repository, click on the plus icon "+" on the top-right corner of the *GitHub* page, on the left of the profile picture icon.

![Click on the plus icon "+" on the top-right corner of the *GitHub* page](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/new-repository.jpg)

This brings you to a page to [create a new *GitHub* repository](https://github.com/new). Provide a name for the *GitHub* repository that you are trying to create. Also, provide a description for the *GitHub* repository. In addition, select either the "Public" or "Private" option for the *GitHub* repository. Furthermore, if you want a new/empty README file for the *GitHub* repository, check the "Initialize this repository with a README" option.

![Create a new *GitHub* repository](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/new-repository-1.jpg)

To avoid committing temporary files associated with the main/primary computer language (supported by *GitHub*) used in your repository, click on the "Add .gitignore: None" button and select one of the computer languages from the drop-down list. If you are using computer languages not supported by *GitHub* in your project/repository, ignore this step.

![Select one of the computer languages from the drop-down list.](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/new-repository-2.jpg)

Click on the "Create repository" button at the bottom of the web page.











###	Modifying A *GitHub* Repository

####	Online (or Web-based) Modifications of A *GitHub* Repository

When viewing a text file in the *GitHub* repository, indicate if the text file can be edited by checking if there is an "editing" icon that is shaped like a pencil/pen. If this "editing" icon exists, click on the "editing" icon to edit the text file. In the picture shown below, this "editing" icon is circled in red.

![Text file that can be edited, and is shown in a panel with an "editing" icon in the top-right corner of the panel](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/initial-repository.jpg)

This brings you to an online text editor to edit the text file, which has read and write permissions, so that the file can be modified and saved online (i.e., commit and push the modification).

![Online text editor to edit a text file](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/editing-readme-file.jpg)

In the text boxes under the "Commit changes" label, write a summary of the modification in the top text box labeled, and write an optional brief description of the modification in the bottom text box. To accept this modification of the file, and commit (or upload) this modification, click on the green "Commit changes" button in the bottom-left corner of the Web page.

![To accept this modification of the file, and commit or upload this modification](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/committing-files.jpg)

The updated README file is shown below.

![updated README file](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/updated-readme-file.jpg)



####	Command-Line Interface -based Modifications of A *GitHub* Repository

To modify a *GitHub* repository using the
	[command-line interface](https://en.wikipedia.org/wiki/Command-line_interface) on [*Unix*-like operating systems](https://en.wikipedia.org/wiki/Unix-like) (such as macOS, [GNU/](https://en.wikipedia.org/wiki/GNU/Linux_naming_controversy)[Linux](https://en.wikipedia.org/wiki/Linux), freeBSD, NetBSD, or Open BSD),
	and upload this modification (via `commit` and `push` commands) to my
		*GitHub* repository,
	run the following sequence of commands.
+ `git add -A` (to add file modifications in the repository to this commit)
+ `git commit -m [Descriptive text for this set of file additions/modifications/deletions]` (commit this set of file modifications to the "holding stage," before this set of modifications is pushed/committed to the *GitHub* repository).
+ `git push`


![Git commit and push](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/git-commit-push-files.jpg)





###	Adding Collaborators to A *GitHub* Repository


To add collaborators to a *GitHub* repository, begin by clicking on the "Settings" tab of the repository, which is the rightmost tab near the top of the web page for the repository. This "Settings" tab is circled in red.

![Click on the "Settings" tab of the repository](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/updated-readme-file.jpg)


On the vertical list/menu beginning with "Options" on the right side of the "Settings" page of the *GitHub* repository, click on the "Collaborators" option. This "Collaborators" option is circled in red.

![click on the "Collaborators" option](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/repository-settings.jpg)

To add collaborators to your *GitHub* repository, enter their *GitHub* username or email addresses associated with their *GitHub* account, and click on the "Add collaborator" button on the center-right side of the page.

![click on the "Add collaborator" button](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/add-collaborators.jpg)





###	Removing Collaborators From A *GitHub* Repository

Go to the "Collaborators" page via the "Settings" page of the *GitHub* repository, and click on the cross on the right side of a collaborator who you want to remove access to the repository.

![Remove collaborator from the repository](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/remove-collaborators.jpg)







###	Creating a New File Online

A new file for your repository can be generated by clicking the "Create new file" button near the top of the repositories.

![Create new file in repositories](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/create-new-file.jpg)

An online text editor would be opened for you to edit/write a text file. This is shown below.

![GitHub online text editor](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/create-new-file-2.jpg)





###	Deleting a File Online

Directory of file to be deleted.

![Directory of file to be deleted](https://github.tamu.edu/zhiyang-ong/ecen-215-spring-2019-lab/blob/master/lab-setup/git-tutorial-pics/file-deletion/directory-of-file-to-be-deleted.jpg)

File to be deleted. Click on the icon of a trash can on the right (circled in red) to delete the file.

![File to be deleted.](https://github.tamu.edu/zhiyang-ong/ecen-215-spring-2019-lab/blob/master/lab-setup/git-tutorial-pics/file-deletion/file-to-be-deleted.jpg)

Deleting file.

![Deleting file - Step 1](https://github.tamu.edu/zhiyang-ong/ecen-215-spring-2019-lab/blob/master/lab-setup/git-tutorial-pics/file-deletion/deleting-file-1.jpg)

Add a comment to describe this file deletion. And, click on the "Commit changes" green button below to confirm deletion of the file.

![Deleting file - Step 2](https://github.tamu.edu/zhiyang-ong/ecen-215-spring-2019-lab/blob/master/lab-setup/git-tutorial-pics/file-deletion/deleting-file-2.jpg)

File deleted.

![File deleted.](https://github.tamu.edu/zhiyang-ong/ecen-215-spring-2019-lab/blob/master/lab-setup/git-tutorial-pics/file-deletion/file-deleted.jpg)

















###	Uploading Files Online

You can upload files for your repository by clicking the "Upload files" button near the top of the repositories.

![Upload files to *Git* repository](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/upload-files.jpg)

Drag files to the shaded region labeled "Drag files here to add them to your repository," or click the hyperlink labeled "choose your files" to select files to be uploaded.

![How to upload files](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/upload-files-2.jpg)




###	Upload Folders/Directories Online

You can also upload folders/directories for your repository by clicking the "Upload files" button near the top of the repositories.

![Upload files to *Git* repository](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/upload-files.jpg)

***Drag folders/directories to the shaded region labeled "Drag files here to add them to your repository."***

Initial Git repository without any syllabus.

![Initial Git repository without any syllabus](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/upload-subdirectory/git-repo-before-uploads.jpg)

Uploaded directory with two syllabi to the Git repository.

![Adding two syllabi to the Git repository](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/upload-subdirectory/add-two-syllabi.jpg)

Added directory with two syllabi.

![Added directory and two syllabi](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/upload-subdirectory/added-directory.jpg)

The two added syllabi.

![The two added syllabi](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/upload-subdirectory/two-syllabi.jpg)

Adding more syllabi to the Git repository, by uploading the modified directory (initial directory with additional files) again.

![Adding more syllabi to the Git repository](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/upload-subdirectory/add-more-syllabi-upload-directory-again.jpg)

***IMPORTANT NOTE!!!: Initial uploaded syllabi were not overwritten.***

The directory/folder is modified. Initial uploaded syllabi were not overwritten.

![Initial uploaded syllabi were not overwritten](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/upload-subdirectory/uploaded-directory.jpg)

Information regarding the initial upload of files is retained, while other files are added to the directory/folder (that was uploaded).

![Information regrading the initial upload of files is retained](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/upload-subdirectory/no-overwrite.jpg)










###	Finding the URL to Clone a *GitHub* Repository

To determine the URL to [clone a *GitHub* repository](https://git-scm.com/book/en/v1/Git-Basics-Getting-a-Git-Repository) by SSH, click on the green "Clone or download" button on the right side of the Web page for the *GitHub* repository. Subsequently, click on the "copy to clipboard" icon to copy the URL (for the SSH protocol).

![Clone with SSH](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/git-clone-ssh.jpg)





To determine the URL to [clone a *GitHub* repository](https://git-scm.com/book/en/v1/Git-Basics-Getting-a-Git-Repository) by [HTTPS](https://help.github.com/articles/cloning-a-repository/), click on the green "Clone or download" button on the right side of the Web page for the *GitHub* repository. Subsequently, click on the "copy to clipboard" icon to copy the URL (for the HTTPS protocol).

![Clone with HTTPS](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/git-clone-https.jpg)




###	Generating SSH Keys

To generate a pair of SSH Keys (i.e., the public key and the corresponding
	private key) for the [Secure Shell protocol, or SSH protocol](https://www.ssh.com/ssh/protocol/)
	from the command line in the *Terminal* application,
	use the `ssh-keygen -f [*location where SSH private and public key would be stored*]/[name associated with this pair of SSH keys] -C [A description that would be associated with this pair of SSH keys]` command.

![Generate SSH keys](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/read-public-ssh-key.jpg)

The contents of the public SHH key can be read as a text file.

![Read public SSH key](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/read-public-ssh-key-2.jpg)


###	Associating SSH Public Keys with a *GitHub* Profile

Go to your *GitHub* profile's "Settings" page, and under the "Personal settings" list on the right, select the "SSH and GPG keys" option. Click on the green "New SSH key" button to add a SSH key to this repository. Also, for each displayed SSH key that is associated with your *GitHub* profile, you can click the grey button with the "Delete" label to dissociate that SSH key from your *GitHub* profile.

![Setting SSH keys](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/settings-ssh-keys.jpg)

When adding a public SSH key to your *GitHub* profile, describe the public SSH key (e.g., the computer account and the computer where its corresponding private SSH key is stored) in the text box labeled "Title" and paste the public SSH key into the text box labeled "Key".

![Adding public SSH key](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/add-ssh-key.jpg)








###	Cloning a *GitHub* Repository by SSH, via the Command-Line Interface

To clone a *GitHub* repository by SSH, via the command-line interface, the following prerequisites/preconditions must be satisfied.
+ A pair of SSH keys (specifically, a public SSH key and a private SSH key) must be associated with SSH connections to the *GitHub* server. See the subsubsection on ["Generating SSH Keys"]() to obtain such pairs of SSH keys.
+ Associate the public SSH key (of any pair of SSH key) for SSH connections from a computer, which contains the associated private SSH key, with your *GitHub* profile. See subsubsection on ["Associating SSH Public Keys with a *GitHub* Profile"]() to do so.




From the command-line interface, use the `git clone [URL of *GitHub* repository for the SSH protocol]` command to clone a *GitHub* repository by SSH.

![CLI command for cloning *GitHub* repository](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/terminal-clone.jpg)



Fix THIS!!!
Do by the weekend.



Visually, the contents of a directory where a *Git*/*GitHub* repository would be clone are shown before and after the cloning process.


Before cloning a *Git*/*GitHub* repository, the contents of the directory are shown below.

![Before cloning Git repository](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/before-clone.jpg)

After cloning a *Git*/*GitHub* repository, the contents of the directory are shown below.

![After cloning Git repository](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/after-clone.jpg)

The contents of the cloned *Git*/*GitHub* repository are shown below.

![Contents of cloned *Git*/*GitHub* repository](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial-pics/administrative-tasks/after-clone-2.jpg)


























###	Documenting Projects

The [Documenting your projects on GitHub](https://guides.github.com/features/wikis/) \cite{GitHubStaff2016c} document shows us how we can document our projects for software development, data science, or otherwise, such that other people can quickly and easily find information that they need about your project/repository.

[\cite{Gruber2004}](http://daringfireball.net/projects/markdown/) is a seminal document on *Markdown*, which we can use as a reference for *Markdown*. *Markdown* provides us with a simple way to document projects hosted in *GitHub* repositories, or other Web-based source-code-hosting service.

Quick look-up references/manuals for *Markdown* are:
+ [\cite{Chapellier2018}](https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md)
+ [\cite{GitHubStaff2014}](https://guides.github.com/features/mastering-markdown/)



###	Miscellaneous Information

Use the [Making Your Code Citable](https://guides.github.com/activities/citable-code/) \cite{GitHubStaff2016d} document to learn how to assign a digital object identifier (DOI), so that a *GitHub* repository can be cited along with its associated research publications.





#	References

BibTeX entries for references that I used.

	@misc{GitHubStaff2016b,
		Address = {San Francisco, {CA}},
		Author = {{GitHub staff}},
		Howpublished = {Available online from {\it GitHub: GitHub Guides} at: \url{https://guides.github.com/activities/hello-world/}; January 24, 2018 was the last accessed date},
		Month = {April 7},
		Publisher = {{GitHub, Inc.}},
		Title = {Hello World},
		Url = {https://guides.github.com/activities/hello-world/},
		Year = {2016}}

	@misc{GitHubStaff20XY,
		Address = {San Francisco, {CA}},
		Author = {{GitHub staff}},
		Howpublished = {Available online from {\it GitHub} at: \url{https://guides.github.com/}; January 24, 2018 was the last accessed date},
		Publisher = {{GitHub, Inc.}},
		Title = {{GitHub} Guides},
		Url = {https://guides.github.com/}}

	@misc{Chapellier2018,
		Address = {San Francisco, {CA}},
		Author = {Cyril Chapellier},
		Howpublished = {Available online from {\it GitHub: tchapi} at: \url{https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md}; December 7, 2018 was the last accessed date},
		Month = {August 20},
		Publisher = {{GitHub, Inc.}},
		Title = {Markdown Cheatsheet: Markdown Cheatsheet for GitHub},
		Url = {https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md},
		Year = {2018}}

	@misc{Nguyen2014,
		Address = {San Francisco, {CA}},
		Author = {Dan Nguyen},
		Howpublished = {Available online from {\it Dan Nguyen's web page} at: \url{https://dannguyen.github.io/github-for-portfolios/}; February 28, 2017 was the last accessed date},
		Month = {April 13},
		Publisher = {{GitHub, Inc.}},
		Title = {Build a Web Portfolio from Scratch: with {Github Pages}},
		Url = {https://dannguyen.github.io/github-for-portfolios/},
		Year = {2014}}

	@misc{Gruber2004,
		Author = {John Gruber},
		Howpublished = {Available online as version 1.0.1 at: \url{http://daringfireball.net/projects/markdown/}; October 9, 2015 was the last accessed date},
		Month = {December 17},
		Publisher = {The Daring Fireball Company {LLC}},
		Title = {Markdown},
		Url = {http://daringfireball.net/projects/markdown/},
		Year = {2004}}

	@book{Kopka2004,
		Address = {Boston, {MA}},
		Author = {Kopka, Helmut and Daly, Patrick W.},
		Edition = {Fourth},
		Publisher = {Addison-Wesley},
		Series = {Addison-Wesley Series on Tools and Techniques for Computer Typesetting},
		Title = {Guide to {\LaTeX}},
		Year = {2004}}

	@misc{GitHubStaff2016d,
		Address = {San Francisco, {CA}},
		Author = {{GitHub staff}},
		Howpublished = {Available online from {\it GitHub: GitHub Guides} at: \url{https://guides.github.com/activities/citable-code/}; January 24, 2018 was the last accessed date},
		Month = {October},
		Publisher = {{GitHub, Inc.}},
		Title = {Making Your Code Citable},
		Url = {https://guides.github.com/activities/citable-code/},
		Year = {2016}}

	@misc{GitHubStaff2016c,
		Address = {San Francisco, {CA}},
		Author = {{GitHub staff}},
		Howpublished = {Available online from {\it GitHub: GitHub Guides} at: \url{https://guides.github.com/features/wikis/}; January 24, 2018 was the last accessed date},
		Month = {July 15},
		Publisher = {{GitHub, Inc.}},
		Title = {Documenting your projects on {GitHub}},
		Url = {https://guides.github.com/features/wikis/},
		Year = {2016}}

	@misc{GitHubStaff2014,
		Address = {San Francisco, {CA}},
		Author = {{GitHub staff}},
		Howpublished = {Available online from {\it GitHub: GitHub Guides} at: \url{https://guides.github.com/features/mastering-markdown/} and \url{https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf}; January 24, 2018 was the last accessed date},
		Month = {January 15},
		Publisher = {{GitHub, Inc.}},
		Title = {Mastering {Markdown}},
		Url = {https://guides.github.com/features/mastering-markdown/},
		Year = {2014}}











##	Notes about In-Text Citation

I use LaTeX and BibTeX notations \cite{Kopka2004} for in-text citations in this document.





















#	Author Information

The MIT License (MIT)

Copyright (c) <2019> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.
